import threading
import queue
from typing import Any, Optional, Callable
from concurrent.futures import ThreadPoolExecutor, Future
from dataclasses import dataclass
from enum import Enum
from loguru import logger

from pyfx.model import Model


class ModelState(Enum):
    CREATED = "created"
    LOADING = "loading"
    READY = "ready"
    SHUTDOWN = "shutdown"


@dataclass
class ModelResult:
    """Result wrapper for threaded model operations"""

    success: bool
    operation_name: str
    data: Any = None
    error: Optional[str] = None
    operation_id: Optional[str] = None


@dataclass
class ProgressUpdate:
    """Progress update for long-running operations"""

    operation_id: str
    progress: float  # 0.0 to 1.0
    message: str
    completed: bool = False


class ModelManager:
    """
    Thread-safe wrapper around Model that runs operations in background thread.

    Provides async interface for JSON processing while maintaining thread safety
    between model operations and UI updates.
    """

    def __init__(self, result_callback, progress_callback, max_workers: int = 2):
        self._executor = ThreadPoolExecutor(
            max_workers=max_workers, thread_name_prefix="pyfx-model"
        )

        # Thread-safe communication
        self._result_queue = queue.Queue()
        self._progress_queue = queue.Queue()
        self._operation_counter = 0
        self._operation_lock = threading.Lock()

        # Callbacks for UI updates
        self._result_callback: Optional[Callable[[ModelResult], None]] = result_callback
        self._progress_callback: Optional[Callable[[ProgressUpdate], None]] = progress_callback

        # Current operation tracking
        self._current_futures: dict[str, Future] = {}

        self._state = ModelState.CREATED
        self._model: Model = Model()

    def load(self, data: Any) -> str:
        """Load data asynchronously"""

        def _load_task(operation_id, operation_name):
            try:
                self._report_progress(operation_id, 0.0, "Initializing model...")

                self._state = ModelState.LOADING
                result = self._model.load(data)

                self._state = ModelState.READY
                self._report_progress(operation_id, 1.0, "Model ready", completed=True)

                model_result = ModelResult(
                    operation_id=operation_id,
                    operation_name=operation_name,
                    success=True,
                    data=result,
                )
                self._report_result(model_result)
            except Exception as e:
                logger.opt(exception=True).error("Load task failed: {}", e)
                self._state = ModelState.SHUTDOWN
                raise

        return self._submit_task("Load", _load_task)

    def query(self, text: str):
        """Execute JSONPath query synchronously"""
        if self._state != ModelState.READY:
            logger.warning(
                "Model not ready for queries, current state: {}", self._state
            )
            return None

        return self._model.query(text)

    def complete(self, text: str):
        """Execute autocompletion synchronously"""
        if self._state != ModelState.READY:
            logger.warning(
                "Model not ready for completion, current state: {}", self._state
            )
            return False, "", []

        return self._model.complete(text)

    def cancel_operation(self, task_id: str) -> bool:
        """Cancel a running operation"""
        if task_id not in self._current_futures:
            return False

        future = self._current_futures[task_id]
        if not future.cancel():
            return False

        del self._current_futures[task_id]
        return True

    def wait_until_ready(self, timeout: float = 10.0) -> bool:
        """Block until model is ready or timeout occurs"""
        import time
        start_time = time.time()

        while self._state != ModelState.READY:
            if time.time() - start_time > timeout:
                logger.warning("Model loading timeout after {}s", timeout)
                return False

            time.sleep(0.01)  # Small sleep to avoid busy waiting

        return True

    def shutdown(self, wait: bool = True):
        """Shutdown the model manager"""
        self._state = ModelState.SHUTDOWN

        # Cancel all pending operations
        for operation_id in list(self._current_futures.keys()):
            self.cancel_operation(operation_id)

        # Shutdown executor
        self._executor.shutdown(wait=wait)

    def _submit_task(self, task_name, task):
        task_id = self.__generate_task_id()

        def wrapped_task():
            try:
                task(task_id, task_name)
            except Exception as e:
                logger.opt(exception=True).error("{} failed: {}", task_name, e)
                self._report_error(
                    task_id, task_name, f"{task_name} failed: {str(e)}"
                )

        future = self._executor.submit(wrapped_task)
        self._current_futures[task_id] = future
        return task_id

    def __generate_task_id(self) -> str:
        """Generate unique operation ID"""
        with self._operation_lock:
            self._operation_counter += 1
            return f"op_{self._operation_counter}"

    def _report_progress(
        self, operation_id: str, progress: float, message: str, completed: bool = False
    ):
        """Report progress update"""
        update = ProgressUpdate(
            operation_id=operation_id,
            progress=progress,
            message=message,
            completed=completed,
        )

        try:
            self._progress_queue.put_nowait(update)
            if self._progress_callback:
                self._progress_callback(update)
        except queue.Full:
            logger.warning("Progress queue full, dropping update")

    def _report_result(self, result: ModelResult):
        """Report operation result"""
        try:
            self._result_queue.put_nowait(result)
            if self._result_callback:
                self._result_callback(result)
        except queue.Full:
            logger.warning("Result queue full, dropping result")

    def _report_error(self, operation_id: str, operation_name: str, error_msg: str):
        """Report operation error"""
        result = ModelResult(
            operation_id=operation_id,
            success=False,
            operation_name=operation_name,
            error=error_msg,
        )
        self._report_result(result)

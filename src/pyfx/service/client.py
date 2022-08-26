import asyncio

from concurrent.futures import ThreadPoolExecutor


class Client:
    def __init__(self, dispatcher):
        self._dispatcher = dispatcher
        self._executor = ThreadPoolExecutor()

    def shutdown(self, wait):
        self._executor.shutdown(wait=wait)

    async def invoke(self, path, *args):
        return await asyncio.get_event_loop().run_in_executor(
            self._executor,
            self._dispatcher.invoke,
            path,
            *args
        )

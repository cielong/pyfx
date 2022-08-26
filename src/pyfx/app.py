"""
Example
=======
.. code-block:: python
   :linenos:

   from pyfx import Controller

   # data is the what you want to render as TUI
   # only supports dict, list and primitive variable
   Controller().run_with_data(data)
"""
from loguru import logger

from .config import Configuration
from .model import Model
from .service.client import Client
from .service.dispatcher import Dispatcher
from .view import View
from .error import PyfxException


class PyfxApp:
    """
    *Pyfx* controller, the main entry point of pyfx library.
    """

    def __init__(self, config=Configuration()):
        self._config = config
        self._dispatcher = Dispatcher()
        self._client = Client(self._dispatcher)
        self._view = View(config.view, self._client)
        self._model = Model(self._dispatcher)

    def run(self, type, *args):
        try:
            data = self._model.load(type, *args)
            self._view.run(data)
        except Exception as e:
            logger.opt(exception=True).\
                error("Unknown exception encountered in app.run, "
                      "exit with {}", e)
            raise PyfxException(f"Unknown error: {e}.")
        finally:
            self._client.shutdown(wait=False)

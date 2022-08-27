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
    *Pyfx* app, the main entry point of pyfx library.

    data: the actual data to be visualized. While the data is supposed to be
          in the JSON format, this requirement is not enforced.
    config: the configuration for Pyfx
    """

    def __init__(self, data, config=Configuration()):
        self._config = config
        self._data = data

        # backend part
        self._dispatcher = Dispatcher()
        # model
        self._model = Model(self._data)
        self._dispatcher.register("query", self._model.query)
        self._dispatcher.register("complete", self._model.complete)

        # UI part
        self._client = Client(self._dispatcher)
        self._view = View(config.view, self._client)

    def run(self):
        try:
            self._view.run(self._data)
        except PyfxException as e:
            # identified exception, will gonna print to stderr
            raise e
        except Exception as e:
            # we gonna swallow unknown error here
            # so that pyfx exit quietly
            logger.opt(exception=True).\
                error("Unknown exception encountered in app.run, "
                      "exit with {}", e)
        finally:
            self._client.shutdown(wait=True)

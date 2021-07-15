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
from .config import Configuration
from .model import Model
from .view import View


class Controller:
    """
    *Pyfx* controller, the main entry point of pyfx library.
    """

    def __init__(self, config=Configuration()):
        self._config = config
        self._view = View(self, config.view)
        self._model = Model(self)

    def run(self, type, *args):
        data = self._model.load(type, *args)
        self._view.run(data)

    def complete(self, text):
        return self._model.complete(text)

    def query(self, text):
        return self._model.query(text)

    def exit(self, exception):
        self._view.exit(exception)

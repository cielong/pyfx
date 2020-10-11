from .model import Model
from .view import View


class Controller:
    """
    `pyfx` controller, the main entry point of this class
    """

    def __init__(self, config_file: str = None):
        self._config = config_file
        self._view = View(self)
        self._model = Model(self)

    def main(self, filename):
        self.run_with_file(filename)

    def run_with_file(self, filename):
        data = self._model.load_data(filename)
        self._view.run(data)

    def run_with_data(self, data):
        self._model.set_data(data)
        self._view.run(data)

    def autocomplete(self, size, widget, text):
        options = self._model.autocomplete(text)
        self._view.enter_autocomplete_popup(size, widget, options)

    def query(self, text):
        data = self._model.query(text)
        self._view.refresh(data)

    def exit(self, exception):
        self._view.exit(exception)

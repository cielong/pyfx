from typing import NoReturn

from .model.model import Model
from .view.view import View


class Controller:
    """
    controller
    """

    def __init__(self, config_file: str = None):
        self._config = config_file
        self._view = View(self)
        self._model = Model(self)

    def main(self, file_name: str) -> NoReturn:
        self._view.run(self._model.load_data(file_name))

    def autocomplete(self, size, widget, text):
        options = self._model.autocomplete(text)
        self._view.enter_autocomplete_popup(size, widget, options)

    def query(self, text):
        data = self._model.query(text)
        self._view.refresh(data)

    def exit(self, exception):
        self._view.exit(exception)

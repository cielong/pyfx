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

    def apply_autocomplete(self, text):
        original_text = self._view.get_query_text()
        data = self._model.apply_autocomplete(original_text + text)
        self._view.exit_autocomplete_popup(data, text)

    def exit(self, exception):
        self._view.exit(exception)

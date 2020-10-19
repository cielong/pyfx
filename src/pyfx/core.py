from .model import Model
from .view import View


class Controller:
    """
    *pyfx* controller, the main entry point of pyfx library.
    """

    def __init__(self, config_file: str = None):
        self._config = config_file
        self._view = View(self)
        self._model = Model(self)

    def run_with_file(self, filename):
        """
        Run *pyfx* with a file in the system.

        :param filename: JSON file path
        :type filename: str
        """
        data = self._model.load_from_file(filename)
        self._view.run(data)

    def run_with_text_stream(self, text_stream):
        """
        Run *pyfx* with a file in the system.

        :param text_stream: JSON file path
        :type text_stream: TextWrapperIO
        """
        data = self._model.load_from_text_stream(text_stream)
        self._view.run(data)

    def run_with_data(self, data):
        """
        Run *pyfx* with data.

        :param data: JSON data
        :type data: dict, list, int, float, str, bool, None
        """
        self._model.load_from_variable(data)
        self._view.run(data)

    def complete(self, widget, text):
        prefix, options = self._model.complete(text)
        if options is None or len(options) == 0:
            return
        self._view.open_autocomplete_popup(prefix, options)

    def query(self, text):
        data = self._model.query(text)
        self._view.refresh(data)

    def exit(self, exception):
        self._view.exit(exception)

from .config import Configuration
from .model import Model
from .view import View


class Controller:
    """
    *pyfx* controller, the main entry point of pyfx library.
    """

    def __init__(self, config=Configuration()):
        self._config = config
        self._view = View(self, config.view)
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

    def run_with_serialized_json(self, text_input):
        """
        Run *pyfx* with serialized json string.
        :param text_input: serialized JSON contents
        :type text_input: str
        """
        data = self._model.load_from_serialized_json(text_input)
        self._view.run(data)

    def run_with_data(self, data):
        """
        Run *pyfx* with data.

        :param data: JSON data
        :type data: dict, list, int, float, str, bool, None
        """
        self._model.load_from_variable(data)
        self._view.run(data)

    def complete(self, text):
        return self._model.complete(text)

    def query(self, text):
        return self._model.query(text)

    def exit(self, exception):
        self._view.exit(exception)

import json
from json import JSONDecodeError

from jsonpath_ng import parse
from loguru import logger

from .autocomplete import autocomplete


class Model:
    """
    pyfx model entry point, which loads and processes JSON data.

    Currently it manages the following actions:
     * loads the original JSON file into memory
     * parses JSONPath query and returns new data
     * performs auto-completion with given JSONPath query
    """

    def __init__(self, controller):
        self._controller = controller
        self._data = None
        self._current = None

    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as f:
                self._data = json.load(f)
        except Exception as e:
            logger.opt(exception=True) \
                .error("Load JSON file {} failed with: {}", file_name, e)
            self._controller.exit(e)

        self._current = self._data
        return self._current

    def load_from_text_stream(self, text_stream):
        try:
            self._data = json.load(text_stream)
        except Exception as e:
            logger.opt(exception=True) \
                .error("Load JSON data from text stream {} failed with: {}", text_stream, e)
            self._controller.exit(e)
        finally:
            text_stream.close()

        self._current = self._data
        return self._current

    def load_from_serialized_json(self, text_input):
        try:
            if text_input != "":
                self._data = json.loads(text_input)
            else:
                self._data = ""
        except JSONDecodeError as e:
            raise e
        except Exception as e:
            logger.opt(exception=True) \
                .error("Load JSON data from serialized json {} failed with: {}", text_input, e)
            self._controller.exit(e)

        self._current = self._data
        return self._current

    def load_from_variable(self, data):
        self._data = data
        self._current = self._data

    def query(self, text):
        if self._data is None:
            logger.info("Data is None.")
            return None

        result = self._query(text)
        self._current = result[0] if len(result) == 1 else result
        return self._current

    # noinspection PyBroadException
    def _query(self, text):
        try:
            jsonpath_expr = parse(text)
            return [match.value for match in jsonpath_expr.find(self._data)]
        except Exception as e:
            logger.opt(exception=True) \
                .error("JSONPath query '{}' failed with: {}", text, e)
            return []

    def complete(self, text):
        if self._data is None:
            logger.info("Data is None.")
            return "", []
        return autocomplete(text, self.query)

import json

from jsonpath_ng import parse
from loguru import logger


class Model:
    """
    pyfx model, it does the following
     * loads the original JSON file into memory
     * parses JSONPath query and returns new data
     * performs autocompletion with given JSONPath query
    """

    def __init__(self,
                 controller: "Controller"
                 ):
        self._controller = controller
        self._data = None
        self._current = None

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as f:
                self._data = json.load(f)
        except Exception as e:
            logger.error("Load JSON file {} failed with: {}", file_name, e)
            self._controller.exit(e)

        self._current = self._data
        return self._current

    def set_data(self, data):
        self._data = data
        self._current = self._data

    def query(self, text):
        if self._data is None:
            logger.info("Data is None.")
            return None

        result = self._query(text)
        self._current = result[0] if len(result) == 1 else result
        return self._current

    def complete(self, text: str):
        if self._data is None:
            logger.info("Data is None.")
            return []

        # TODO: find last dot in the JSONPath,
        #  this is in fact not a valid way to find the nearest workable part
        last_dot_index = text.rindex('.')
        result = self._query(text[:last_dot_index])
        if len(result) > 1:
            options = ['*']
            options.extend([str(index) for index in range(len(result))])
            options = filter(lambda o: o.startswith(text[last_dot_index + 1:]), options)
            return list(options)
        elif len(result) == 1:
            result = result[0]
            if isinstance(result, list):
                options = ['*']
                options.extend([str(index) for index in range(len(result))])
                options = filter(lambda o: o.startswith(text[last_dot_index + 1:]), options)
                return list(options)
            elif isinstance(result, dict):
                options = [k for k in result.keys()]
                options = filter(lambda o: o.startswith(text[last_dot_index + 1:]), options)
                return list(options)
        return []

    # noinspection PyBroadException
    def _query(self, text):
        try:
            jsonpath_expr = parse(text)
            return [match.value for match in jsonpath_expr.find(self._data)]
        except Exception as e:
            logger.error("JSONPath query '{}' failed with: {}", text, e)
            return []

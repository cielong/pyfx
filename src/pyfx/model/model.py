from jsonpath_ng import parse
from loguru import logger

from .autocomplete import autocomplete
from .io.datasource import create_data_source


class Model:
    """
    pyfx model entry point, which loads and processes JSON data.

    Currently it manages the following actions:
     * loads the original JSON file into memory
     * parses JSONPath query and returns new data
     * performs auto-completion with given JSONPath query
    """

    def __init__(self, dispatcher):
        self._data = None
        self._current = None
        dispatcher.register("load", self.load)
        dispatcher.register("query", self.query)
        dispatcher.register("complete", self.complete)

    def load(self, type, *args):
        datasource = create_data_source(type)(*args)
        self._data = datasource.read_json()
        self._current = self._data
        return self._current

    def query(self, text):
        if self._data is None:
            logger.debug("Data is None.")
            return None

        result = self._query(text)
        self._current = result[0] if len(result) == 1 else result
        return self._current

    def complete(self, text):
        if self._data is None:
            logger.debug("Data is None.")
            return False, "", []
        return autocomplete(text, self.query)

    # noinspection PyBroadException
    def _query(self, text):
        try:
            jsonpath_expr = parse(text)
            return [match.value for match in jsonpath_expr.find(self._data)]
        except Exception as e:
            logger.opt(exception=True) \
                .error("JSONPath query '{}' failed with: {}", text, e)
            return []

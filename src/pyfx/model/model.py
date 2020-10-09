import json
from jsonpath_ng import parse


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
            self._controller.exit(e)

        self._current = self._data
        return self._current

    def set_data(self, data):
        self._data = data
        self._current = self._data

    def query(self, text):
        if self._data is None:
            return None
        # noinspection PyBroadException
        try:
            jsonpath_expr = parse(text)
            self._current = [match.value for match in jsonpath_expr.find(self._data)]
            self._current = self._current[0] if len(self._current) == 1 else self._current
            return self._current
        except Exception:
            return None

    def autocomplete(self, text):
        segments = self._parse(text)
        if self._data is None:
            return []

        try:
            current = self._data
            current_options = self._find_options(current)
            for segment in segments:
                if segment == "":
                    continue
                current = current[segment]
                current_options = self._find_options(current)

            return current_options
        except KeyError:
            return []

    def _find_options(self, current):
        if isinstance(current, list):
            return [o for c in current for o in self._find_options(c)]
        elif isinstance(current, dict):
            return [k for k in current.keys()]
        else:
            return [""]

    def _parse(self, text: str):
        segments = text.split('.')
        return segments

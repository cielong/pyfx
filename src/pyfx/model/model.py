import json


class Model:
    """
    model
    """

    def __init__(self,
                 controller: "Controller"
                 ):
        self._controller = controller
        self._data = None

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as f:
                self._data = json.load(f)
        except Exception as e:
            self._controller.exit(e)

        return self._data

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

    def apply_autocomplete(self, text):
        segments = self._parse(text)
        if self._data is None:
            return None

        try:
            current = self._data
            for segment in segments:
                if segment == "":
                    continue
                current = current[segment]
            return current
        except KeyError:
            return None

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

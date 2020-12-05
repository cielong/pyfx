from overrides import overrides

from ..json_widget import JSONWidget


class ArrayStartWidget(JSONWidget):
    """
    display widget for JSON `array` type node
    """

    def __init__(self, node, display_key):
        super().__init__(node, True, display_key)

    @overrides
    def load_value_markup(self):
        return "["

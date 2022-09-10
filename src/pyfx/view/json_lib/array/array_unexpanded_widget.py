from overrides import overrides

from ..json_widget import JSONWidget


class ArrayUnexpandedWidget(JSONWidget):
    """The widget to display when an `array` type JSON node is not expanded."""

    def __init__(self, node, display_key):
        super().__init__(node, True, display_key)

    @overrides
    def load_value_markup(self):
        return "[\u2026]"

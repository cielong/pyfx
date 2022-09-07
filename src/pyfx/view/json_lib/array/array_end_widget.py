from overrides import overrides

from ..json_widget import JSONWidget


class ArrayEndWidget(JSONWidget):
    """The widget for the ending edge of an `array` type JSON node."""

    def __init__(self, node):
        # display_key is not important for end widget
        super().__init__(node, True, False)

    @overrides
    def load_value_markup(self):
        return "]"

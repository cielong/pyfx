from overrides import overrides

from ..json_widget import JSONWidget


class ObjectEndWidget(JSONWidget):
    """The widget for the ending edge of an `object` type JSON node."""

    def __init__(self, node):
        super().__init__(node, True, False)

    @overrides
    def load_value_markup(self):
        return "}"

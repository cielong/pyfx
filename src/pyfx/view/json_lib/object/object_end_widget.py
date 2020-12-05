from overrides import overrides

from ..json_widget import JSONWidget


class ObjectEndWidget(JSONWidget):
    """
    a widget to display the end symbol for JSON `object` type nodes
    """

    def __init__(self, node):
        super().__init__(node, True, False)

    @overrides
    def load_value_markup(self):
        return "}"

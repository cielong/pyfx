from overrides import overrides

from ..json_widget import JSONWidget


class ObjectStartWidget(JSONWidget):
    """
    a widget to display start text if expanded for JSON `object` type nodes
    """

    def __init__(self, node, display_key):
        super().__init__(node, True, display_key)

    @overrides
    def load_value_markup(self):
        return "{"

from overrides import overrides

from ..json_widget import JSONWidget


class PrimitiveWidget(JSONWidget):
    """A base widget to display primitive JSON types."""

    def __init__(self, node, display_key):
        super().__init__(node, False, display_key)

    @overrides
    def load_value_markup(self):
        return str(self.get_node().get_value())

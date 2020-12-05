from overrides import overrides

from ..json_widget import JSONWidget


class ObjectUnexpandedWidget(JSONWidget):
    """
    a widget to display unexpanded text for JSON `object` type nodes
    """

    def __init__(self,
                 node,
                 display_key,
                 ):
        super().__init__(node, True, display_key)

    @overrides
    def load_value_markup(self):
        return "{\u2026}"

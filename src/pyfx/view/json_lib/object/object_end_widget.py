from overrides import overrides

from ..json_widget import JSONWidget
from ...common import SelectableText


class ObjectEndWidget(JSONWidget):
    """
    a widget to display the end symbol for JSON `object` type nodes
    """

    def __init__(self, node):
        super().__init__(node, True, False)

    @overrides
    def load_inner_widget(self):
        return SelectableText("}")

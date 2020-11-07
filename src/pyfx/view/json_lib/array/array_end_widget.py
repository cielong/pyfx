from overrides import overrides

from ..json_widget import JSONWidget
from ...common import SelectableText


class ArrayEndWidget(JSONWidget):
    """
    display widget for JSON `array` type node
    """

    def __init__(self, node):
        # display_key is not important for end widget
        super().__init__(node, True, False)

    @overrides
    def load_inner_widget(self):
        return SelectableText("]")

import urwid
from overrides import overrides

from ..json_widget import JSONWidget
from ...common import SelectableText


class ArrayStartWidget(JSONWidget):
    """
    display widget for JSON `array` type node
    """

    def __init__(self, node, display_key):
        super().__init__(node, True, display_key)

    @overrides
    def load_inner_widget(self):
        if not self.is_display_key():
            return SelectableText("[")

        return urwid.Columns([
            ('pack', SelectableText([('key', self.get_node().get_key()), ": "])),
            SelectableText("[")
        ])

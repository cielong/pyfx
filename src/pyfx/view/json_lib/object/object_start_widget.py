import urwid
from overrides import overrides

from ..json_widget import JSONWidget
from ...common import SelectableText


class ObjectStartWidget(JSONWidget):
    """
    a widget to display start text if expanded for JSON `object` type nodes
    """

    def __init__(self, node, display_key):
        super().__init__(node, True, display_key)

    @overrides
    def load_inner_widget(self):
        if not self.is_display_key():
            return SelectableText("{")

        return urwid.Columns([
            ('pack', SelectableText([('key', self.get_node().get_key()), ": "])),
            SelectableText("{")
        ])

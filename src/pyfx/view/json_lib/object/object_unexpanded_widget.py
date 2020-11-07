import urwid
from overrides import overrides

from ..json_widget import JSONWidget
from ...common import SelectableText


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
    def load_inner_widget(self):
        if not self.is_display_key():
            return SelectableText("{\u2026}")

        return urwid.Columns([
            ('pack', SelectableText([('key', self.get_node().get_key()), ": "])),
            SelectableText("{\u2026}")
        ])

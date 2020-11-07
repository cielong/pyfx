import urwid
from overrides import overrides

from ..json_widget import JSONWidget
from ...common import SelectableText


class PrimitiveWidget(JSONWidget):
    """
    a widget to display JSON `string`, `integer`, `number`, `boolean`, `null` type
    """

    def __init__(self,
                 node,
                 display_key
                 ):
        super().__init__(node, False, display_key)

    @overrides
    def load_inner_widget(self):
        key = self.get_node().get_key()

        value = self.get_node().get_value()
        value = 'null' if value is None else value

        if not self.is_display_key():
            return SelectableText(f"{value}")

        # FIXME: urwid.Columns will discard the calculated column if the column width is 0,
        #  regardless of whether the column itself has 0 width or it does not fit the whole row
        return urwid.Columns([
            ('pack', SelectableText([('key', f"{key}"), ": "])),
            SelectableText(f"{value}")
        ])

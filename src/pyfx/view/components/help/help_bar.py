import urwid


class HelpBar(urwid.WidgetWrap):
    """
    A text widget to display short help string.
    """

    def __init__(self, short_help):
        self._text_widget = urwid.Text(short_help)
        super().__init__(urwid.AttrMap(self._text_widget, "foot"))

import urwid


class HelpBar(urwid.WidgetWrap):
    HELP_TEXT = [
        ('title', "Pyfx"), "    ", "UP, DOWN, ENTER, Q",
    ]

    def __init__(self, manager):
        self._manager = manager
        self._text_widget = urwid.Text(HelpBar.HELP_TEXT)
        super().__init__(urwid.AttrMap(self._text_widget, "foot"))

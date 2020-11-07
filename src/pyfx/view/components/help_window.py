import urwid


class HelpWindow(urwid.WidgetWrap):
    HELP_TEXT = [
            ('title', "Pyfx"), "    ", "UP, DOWN, ENTER, Q",
        ]

    def __init__(self, manager):
        self._manager = manager
        self._text_widget = urwid.Text(HelpWindow.HELP_TEXT)
        super().__init__(urwid.AttrWrap(self._text_widget, "foot"))

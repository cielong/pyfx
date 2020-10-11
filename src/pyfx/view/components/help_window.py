import urwid


class HelpWindow(urwid.WidgetWrap):
    HELP_TEXT = [
            ('title', "Pyfx"), "    ",
            ('key', "UP"), ",", ('key', "DOWN"), ",",
            ('key', "ENTER"), "  ",
            ('key', "Q"),
        ]

    def __init__(self):
        self._text_widget = urwid.Text(HelpWindow.HELP_TEXT)
        super().__init__(urwid.AttrWrap(self._text_widget, "foot"))

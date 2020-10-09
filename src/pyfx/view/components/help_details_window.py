import urwid


class HelpDetailsWindow(urwid.WidgetWrap):
    HELP_TEXT = ""

    def __init__(self):
        self._text_widget = urwid.AttrWrap(
            urwid.ListBox(urwid.SimpleListWalker([urwid.Text(HelpDetailsWindow.HELP_TEXT)])),
            "body"
        )
        super().__init__(self._text_widget)

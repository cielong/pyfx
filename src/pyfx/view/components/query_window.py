import urwid


class QueryWindow(urwid.WidgetWrap):
    """
    Query window for `pyfx` to input JSONPath query
    """

    JSONPATH_START = "$"

    def __init__(self, controller):
        self._controller = controller
        self._edit_widget = urwid.Edit(QueryWindow.JSONPATH_START)
        super().__init__(urwid.AttrWrap(self._edit_widget, None, "focus"))

    def setup(self, size):
        # urwid.connect_signal(self._edit_widget, "change", self._callback, user_args=[size])
        pass

    def reset(self):
        # urwid.disconnect_signal(self._edit_widget, "change", self._callback)
        pass

    def get_text(self):
        return self._edit_widget.get_text()[0]

    def insert_edit_text(self, text: str):
        self._edit_widget.insert_text(text)

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == 'enter':
            self._controller.query(self.get_text())
        elif key == 'esc':
            self._controller.query(self.get_text())
        return key

import urwid


class QueryWindow(urwid.WidgetWrap):
    EMPTY_TEXT = ""

    def __init__(self, callback):
        self._callback = callback
        self._edit_widget = urwid.Edit()
        super().__init__(urwid.AttrWrap(self._edit_widget, None, "focus"))

    def setup(self, size):
        urwid.connect_signal(self._edit_widget, "change", self._callback, user_args=[size])

    def get_edit_text(self):
        return self._edit_widget.get_edit_text()

    def set_edit_text(self, text: str):
        self._edit_widget.insert_text(text)

    def reset(self):
        urwid.disconnect_signal(self._edit_widget, "change", self._callback)
        self._edit_widget.set_edit_text(QueryWindow.EMPTY_TEXT)

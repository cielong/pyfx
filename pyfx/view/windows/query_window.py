import urwid


class QueryWindow(urwid.WidgetWrap):
    EMPTY_TEXT = ""

    def __init__(self, callback):
        self._callback = callback
        self._edit_widget = urwid.Edit()
        super().__init__(urwid.AttrWrap(self._edit_widget, None, "focus"))

    def setup(self):
        urwid.connect_signal(self._edit_widget, "change", self._callback)

    def reset(self):
        urwid.disconnect_signal(self._edit_widget, "change", self._callback)
        self._edit_widget.set_edit_text(QueryWindow.EMPTY_TEXT)

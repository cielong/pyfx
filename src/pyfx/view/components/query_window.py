import urwid


class QueryWindow(urwid.WidgetWrap):
    """
    Query window for `pyfx` to input JSONPath query
    """

    JSONPATH_START = "$"

    def __init__(self, callback):
        self._callback = callback
        self._edit_widget = urwid.Edit(QueryWindow.JSONPATH_START)
        super().__init__(urwid.AttrWrap(self._edit_widget, None, "focus"))

    def setup(self, size):
        urwid.connect_signal(self._edit_widget, "change", self._callback, user_args=[size])

    def reset(self):
        urwid.disconnect_signal(self._edit_widget, "change", self._callback)
        self._edit_widget.edit_text = QueryWindow.JSONPATH_START

    def get_edit_text(self):
        return self._edit_widget.get_edit_text()

    def insert_edit_text(self, text: str):
        self._edit_widget.insert_text(text)

    def keypress(self):
        key = super().keypress()
        return key

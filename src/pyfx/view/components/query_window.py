import urwid
from overrides import overrides


class QueryWindow(urwid.WidgetWrap):
    """
    Query window for `pyfx` to input JSONPath query
    """

    JSONPATH_START = "$"

    def __init__(self, manager, controller):
        self._manager = manager
        self._controller = controller
        self._edit_widget = urwid.Edit()
        self._edit_widget.insert_text(QueryWindow.JSONPATH_START)
        super().__init__(urwid.AttrWrap(self._edit_widget, None, "focus"))

    def setup(self):
        urwid.signals.connect_signal(self._edit_widget, 'change', self._controller.complete)

    def reset(self):
        urwid.signals.disconnect_signal(self._edit_widget, 'change', self._controller.complete)

    def get_text(self):
        return self._edit_widget.get_text()[0]

    def insert_text(self, text: str):
        self._edit_widget.insert_text(text)

    def keypress_internal(self, key):
        # the query window is placed at the footer of the view_frame, thus
        # use the screen size is enough
        max_col, max_row = self._manager.size()
        self.keypress((max_col, ), key)

    @overrides
    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == 'enter':
            self._controller.query(self.get_text())
            self._manager.enter_view_window()
        elif key == 'esc':
            self._controller.query(self.get_text())
            self._manager.exit_query_window()
        return key

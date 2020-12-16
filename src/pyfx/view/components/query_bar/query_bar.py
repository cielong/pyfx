from enum import Enum

import urwid
from overrides import overrides


class QueryBarKeys(Enum):
    QUERY = "enter"
    CANCEL = "esc"


class QueryBar(urwid.WidgetWrap):
    """
    Query window for `pyfx` to input JSONPath query
    """

    JSONPATH_START = "$"

    def __init__(self, mediator, controller, keymapper):
        self._mediator = mediator
        self._controller = controller
        self._keymapper = keymapper
        self._edit_widget = urwid.Edit()
        self._edit_widget.insert_text(QueryBar.JSONPATH_START)
        super().__init__(urwid.AttrMap(self._edit_widget, None, "focus"))

    def setup(self):
        urwid.signals.connect_signal(self._edit_widget, 'change', self.complete)

    def reset(self):
        urwid.signals.disconnect_signal(self._edit_widget, 'change', self.complete)

    def complete(self, widget, text):
        is_partial_complete, prefix, options = self._controller.complete(text)
        if options is None or len(options) == 0:
            return
        self._mediator.notify("query_bar", "popup", prefix, options, is_partial_complete)

    def get_text(self):
        return self._edit_widget.get_text()[0]

    def insert_text(self, text, is_partial_complete):
        self.reset()
        self._edit_widget.insert_text(text)
        if is_partial_complete:
            self.setup()
            return
        data = self._controller.query(self.get_text())
        self._mediator.notify("query_bar", "query_result", data)
        self.setup()

    def pass_keypress(self, key):
        max_col, max_row = self._mediator.notify("query_bar", "size")
        self.keypress((max_col, ), key)

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == QueryBarKeys.QUERY.value:
            data = self._controller.query(self.get_text())
            self._mediator.notify("query_bar", "query_result", data)
            self._mediator.notify("query_bar", "switch")
            return

        if key == QueryBarKeys.CANCEL.value:
            data = self._controller.query(self.get_text())
            self._mediator.notify("query_bar", "query_result", data)
            self._mediator.notify("query_bar", "switch")
            return

        return key

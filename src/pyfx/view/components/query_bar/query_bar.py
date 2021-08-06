import asyncio
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

    def __init__(self, mediator, client, keymapper):
        self._client = client
        self._mediator = mediator
        self._keymapper = keymapper
        self._edit_widget = urwid.Edit()
        self._edit_widget.insert_text(QueryBar.JSONPATH_START)
        super().__init__(urwid.AttrMap(self._edit_widget, None, "focus"))

        self._mediator.register("select_complete_option", self.insert_text)
        self._mediator.register("keypress", self.pass_keypress)

    def setup(self):
        urwid.signals.connect_signal(
            self._edit_widget, 'change', self.complete
        )

    def reset(self):
        urwid.signals.disconnect_signal(
            self._edit_widget, 'change', self.complete
        )

    def complete(self, widget, text):
        is_partial_complete, prefix, options = asyncio.get_event_loop(). \
            run_until_complete(
            self._client.invoke("complete", text)
        )
        if options is None or len(options) == 0:
            return
        self._mediator.notify(
            "open_pop_up",
            "query_bar",
            prefix,
            options,
            is_partial_complete
        )

    def get_text(self):
        return self._edit_widget.get_text()[0]

    def insert_text(self, text, is_partial_complete):
        self.reset()
        self._edit_widget.insert_text(text)
        if is_partial_complete:
            self.setup()
            return
        data = asyncio.get_event_loop().run_until_complete(
            self._client.invoke("query", self.get_text())
        )
        self._mediator.notify("refresh_view", "query_bar", data)
        self.setup()

    def pass_keypress(self, key):
        max_col, max_row = self._mediator.notify(
            "get_component_size", "query_bar"
        )[0]
        self.keypress((max_col,), key)

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == QueryBarKeys.QUERY.value:
            data = asyncio.get_event_loop().run_until_complete(
                self._client.invoke("query", self.get_text())
            )
            self._mediator.notify("refresh_view", "query_bar", data)
            self._mediator.notify("focus_on_view", "query_bar")
            return

        if key == QueryBarKeys.CANCEL.value:
            data = asyncio.get_event_loop().run_until_complete(
                self._client.invoke("query", self.get_text())
            )
            self._mediator.notify("refresh_view", "query_bar", data)
            self._mediator.notify("focus_on_view", "query_bar")
            return

        return key

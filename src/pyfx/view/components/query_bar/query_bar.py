import asyncio
from enum import Enum

import urwid
from loguru import logger
from overrides import overrides
from ...keymapper import KeyDefinition


class QueryBarKeys(KeyDefinition, Enum):
    QUERY = "enter", "Execute the current query and back to JSON browser."
    CANCEL = "esc", "Exit query bar and back to JSON browser."


class QueryBar(urwid.WidgetWrap):
    """
    Query window for `pyfx` to input JSONPath query.
    """

    JSONPATH_START = "$"

    def __init__(self, mediator, client, keymapper):
        self._client = client
        self._mediator = mediator
        self._keymapper = keymapper
        self._edit_widget = urwid.Edit()
        self._edit_widget.insert_text(QueryBar.JSONPATH_START)
        self.setup()
        super().__init__(urwid.AttrMap(self._edit_widget, None, "focus"))

    def setup(self):
        urwid.signals.connect_signal(
            self._edit_widget, 'change', self.complete
        )

    def reset(self):
        urwid.signals.disconnect_signal(
            self._edit_widget, 'change', self.complete
        )

    def complete(self, widget, text):
        try:
            # TODO: make the wait time configurable
            # wait at most 200 ms, so that UI is not freeze
            is_partial_complete, prefix, options = \
                self._client.invoke_with_timeout(0.2, "complete", text)
        except asyncio.TimeoutError:
            logger.info(f"Auto-completion timeout with text {text}.")
            return
        if options is None or len(options) == 0:
            return
        self._mediator.notify(
            "query_bar", "open_pop_up", prefix, options,
            is_partial_complete, pop_up_type="autocomplete")

    def get_text(self):
        return self._edit_widget.get_text()[0]

    def insert_text(self, text, is_partial_complete):
        self.reset()
        self._edit_widget.insert_text(text)
        if is_partial_complete:
            self.setup()
            return
        data = self._client.invoke("query", self.get_text())
        self._mediator.notify("query_bar", "refresh_view", data)
        self.setup()

    def pass_keypress(self, key):
        max_col, max_row = self._mediator.notify(
            "query_bar", "size", "query_bar"
        )[0][1]
        self.keypress((max_col,), key)

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == QueryBarKeys.QUERY.key:
            data = self._client.invoke("query", self.get_text())
            self._mediator.notify("query_bar", "refresh_view", data)
            self._mediator.notify("query_bar", "focus", "json_browser")
            return

        if key == QueryBarKeys.CANCEL.key:
            data = self._client.invoke("query", self.get_text())
            self._mediator.notify("query_bar", "refresh_view", data)
            self._mediator.notify("query_bar", "focus", "json_browser")
            return

        return key

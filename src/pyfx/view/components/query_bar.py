import asyncio
from dataclasses import dataclass
from enum import Enum

import urwid
from loguru import logger
from overrides import overrides

from pyfx.view.components.abstract_component_keys import BaseComponentKeyMapper
from pyfx.view.components.abstract_component_keys import KeyDefinition


class QueryBarKeys(KeyDefinition, Enum):
    """Enums for all the available keys defined in QueryBar."""

    QUERY = "enter", "Execute the current query and back to JSON browser."
    CANCEL = "esc", "Exit query bar and back to JSON browser."


@dataclass(frozen=True)
class QueryBarKeyMapper(BaseComponentKeyMapper):
    query: str = "enter"
    cancel: str = "esc"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.query: QueryBarKeys.QUERY,
            self.cancel: QueryBarKeys.CANCEL
        }

    @property
    @overrides
    def short_help(self):
        return [f"QUERY: {self.query}",
                f"CANCEL: {self.cancel}"]

    @property
    @overrides
    def detailed_help(self):
        keys = [self.query, self.cancel]
        descriptions = {key: self.mapped_key[key].description for key in keys}
        return {
            "section": "Query Bar",
            "description": descriptions
        }


class QueryBar(urwid.WidgetWrap):
    """The window to write JsonPath query."""

    JSONPATH_START = "$"

    def __init__(self, mediator, client, keymapper):
        self._client = client
        self._mediator = mediator
        self._keymapper = keymapper
        self._edit_widget = urwid.Edit()
        self._edit_widget.insert_text(QueryBar.JSONPATH_START)
        self.setup()
        super().__init__(self._edit_widget)

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
            msg = f"Auto-completion timeout with text {text}."
            self._mediator.notify("query_bar", "update", "warning_bar", msg)
            self._mediator.notify("query_bar", "show", "view_frame",
                                  "warning_bar", False)
            logger.info(msg)
            return
        if options is None or len(options) == 0:
            return
        self._mediator.notify(
            "query_bar", "open_pop_up", "view_frame", prefix, options,
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
        self._mediator.notify("query_bar", "refresh", "json_browser", data)
        self.setup()

    def pass_keypress(self, key):
        max_col, max_row = self._mediator.notify("query_bar", "size",
                                                 "view_frame", "query_bar")
        self.handle_keypress((max_col,), key)

    def help_message(self):
        return self._keymapper.short_help

    @overrides
    def keypress(self, size, key):
        # FIXME: A very hacky way to deal with two cases of key press handling
        #  in query bar
        key = self.handle_keypress(size, key)

        if key is None:
            return None

        self._mediator.notify("query_bar", "update", "warning_bar",
                              f"Unknown key `{key}`. Press any keys to "
                              f"continue.")
        self._mediator.notify("query_bar", "show", "view_frame", "warning_bar",
                              False)

        return key

    def handle_keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key is None:
            return None

        if key == QueryBarKeys.QUERY.key:
            data = self._client.invoke("query", self.get_text())
            self._mediator.notify("query_bar", "refresh", "json_browser", data)
            self._mediator.notify("query_bar", "show", "view_frame",
                                  "json_browser", True)
            return None

        if key == QueryBarKeys.CANCEL.key:
            data = self._client.invoke("query", self.get_text())
            self._mediator.notify("query_bar", "refresh", "json_browser", data)
            self._mediator.notify("query_bar", "show", "view_frame",
                                  "json_browser", True)
            return None

        return key

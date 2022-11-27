from dataclasses import dataclass
from enum import Enum

import urwid
from overrides import overrides

from pyfx.view.json_lib import JSONListBox
from pyfx.view.json_lib import JSONListWalker
from pyfx.view.components.abstract_component_keys import BaseComponentKeyMapper
from pyfx.view.components.abstract_component_keys import KeyDefinition


class JSONBrowserKeys(KeyDefinition, Enum):
    """Enums for all the available keys defined in JSONBrowser."""

    # keys for json lib
    CURSOR_UP = "up", "Move cursor up from the current line."
    CURSOR_DOWN = "down", "Move cursor down from the current line."
    COLLAPSE_ALL = "c", "Collapse all the node."
    EXPAND_ALL = "e", "Expand all the node."
    TOGGLE_EXPANSION = "enter", \
                       "Toggle to expand/collapse the current JSON node."

    # keys for switching window
    OPEN_QUERY_BAR = ".", "Open the query bar to type JSONPath."
    OPEN_HELP_PAGE = "?", "Open help page."

    # keys for exit Pyfx
    EXIT = "q", "Quit Pyfx."


@dataclass(frozen=True)
class JSONBrowserKeyMapper(BaseComponentKeyMapper):
    exit: str = "q"

    open_help_page: str = "?"
    open_query_bar: str = "."

    cursor_up: str = "up"
    cursor_down: str = "down"
    toggle_expansion: str = "enter"
    expand_all: str = "e"
    collapse_all: str = "c"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.cursor_up: JSONBrowserKeys.CURSOR_UP,
            self.cursor_down: JSONBrowserKeys.CURSOR_DOWN,
            self.toggle_expansion: JSONBrowserKeys.TOGGLE_EXPANSION,
            self.expand_all: JSONBrowserKeys.EXPAND_ALL,
            self.collapse_all: JSONBrowserKeys.COLLAPSE_ALL,
            self.open_query_bar: JSONBrowserKeys.OPEN_QUERY_BAR,
            self.open_help_page: JSONBrowserKeys.OPEN_HELP_PAGE,
            self.exit: JSONBrowserKeys.EXIT
        }

    @property
    @overrides
    def short_help(self):
        return [f"UP: {self.cursor_up}",
                f"DOWN: {self.cursor_down}",
                f"TOGGLE: {self.toggle_expansion}",
                f"QUERY: {self.open_query_bar}",
                f"HELP: {self.open_help_page}",
                f"QUIT: {self.exit}"]

    @property
    @overrides
    def detailed_help(self):
        keys = [
            self.exit,
            self.cursor_up, self.cursor_down, self.toggle_expansion,
            self.expand_all, self.collapse_all,
            self.open_query_bar, self.open_help_page
        ]
        descriptions = {key: self.mapped_key[key].description for key in keys}
        return {
            "section": "JSON Browser",
            "description": descriptions
        }


class JSONBrowser(urwid.WidgetWrap):
    """The main view window to display JSON contents."""

    def __init__(self, node_factory, mediator, keymapper):
        self._node_factory = node_factory
        self._keymapper = keymapper
        self._mediator = mediator
        super().__init__(self._load_widget(None))

    def refresh_view(self, data):
        self._w = self._load_widget(data)

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key is None:
            return None

        if key == JSONBrowserKeys.EXIT.key:
            raise urwid.ExitMainLoop()

        if key == JSONBrowserKeys.OPEN_QUERY_BAR.key:
            self._mediator.notify("json_browser", "show", "view_frame",
                                  "query_bar", True)
            return None

        if key == JSONBrowserKeys.OPEN_HELP_PAGE.key:
            self._mediator.notify("json_browser", "open_pop_up", "view_frame",
                                  pop_up_type="help")
            return None

        self._mediator.notify("json_browser", "update", "warning_bar",
                              f"Unknown key `{key}`. Press `?` for all "
                              f"supported keys.")
        self._mediator.notify("json_browser", "show", "view_frame",
                              "warning_bar", False)

        return key

    def help_message(self):
        return self._keymapper.short_help

    def _load_widget(self, data):
        listbox = JSONListBox(JSONListWalker(
            data, node_factory=self._node_factory))
        return listbox

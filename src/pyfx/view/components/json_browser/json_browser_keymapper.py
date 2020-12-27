from dataclasses import dataclass

from overrides import overrides

from .json_browser import JSONBrowserKeys
from ...keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class JSONBrowserKeyMapper(AbstractComponentKeyMapper):
    cursor_up: str = "up"
    cursor_down: str = "down"
    toggle_expansion: str = "enter"
    expand_all: str = "e"
    collapse_all: str = "c"
    open_query_bar: str = "."

    @property
    @overrides
    def mapped_key(self):
        return {
            self.cursor_up: JSONBrowserKeys.CURSOR_UP,
            self.cursor_down: JSONBrowserKeys.CURSOR_DOWN,
            self.toggle_expansion: JSONBrowserKeys.TOGGLE_EXPANSION,
            self.open_query_bar: JSONBrowserKeys.OPEN_QUERY_BAR,
            self.expand_all: JSONBrowserKeys.EXPAND_ALL,
            self.collapse_all: JSONBrowserKeys.COLLAPSE_ALL
        }

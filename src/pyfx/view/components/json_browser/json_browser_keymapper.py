from dataclasses import dataclass

from overrides import overrides

from .json_browser import JSONBrowserKeys
from ...keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class JSONBrowserKeyMapper(AbstractComponentKeyMapper):
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

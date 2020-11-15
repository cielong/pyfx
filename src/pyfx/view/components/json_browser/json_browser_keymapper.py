from dataclasses import dataclass

from overrides import overrides

from .json_browser import JSONBrowserKeys
from ...keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class JSONBrowserKeyMapper(AbstractComponentKeyMapper):
    cursor_up: str = "up"
    cursor_down: str = "down"
    toggle_expansion: str = "enter"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.cursor_up: JSONBrowserKeys.CURSOR_UP,
            self.cursor_down: JSONBrowserKeys.CURSOR_DOWN,
            self.toggle_expansion: JSONBrowserKeys.TOGGLE_EXPANSION
        }

from dataclasses import dataclass

from overrides import overrides

from .autocomplete_popup import AutoCompletePopUpKeys
from ...keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class AutoCompletePopUpKeyMapper(AbstractComponentKeyMapper):

    cursor_up: str = "up"
    cursor_down: str = "down"
    select: str = "enter"
    cancel: str = "esc"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.cursor_up: AutoCompletePopUpKeys.CURSOR_UP,
            self.cursor_down: AutoCompletePopUpKeys.CURSOR_DOWN,
            self.select: AutoCompletePopUpKeys.SELECT,
            self.cancel: AutoCompletePopUpKeys.CANCEL
        }

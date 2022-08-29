from dataclasses import dataclass

from overrides import overrides

from .help_popup import HelpPopUpKeys
from ...keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class HelpPopUpKeyMapper(AbstractComponentKeyMapper):
    cursor_up: str = "up"
    cursor_down: str = "down"
    exit: str = "esc"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.cursor_up: HelpPopUpKeys.CURSOR_UP,
            self.cursor_down: HelpPopUpKeys.CURSOR_DOWN,
            self.exit: HelpPopUpKeys.EXIT,
        }

    @property
    @overrides
    def detailed_help(self):
        keys = [
            self.cursor_up, self.cursor_down, self.exit
        ]
        descriptions = {key: self.mapped_key[key].description for key in keys}
        return {
            "section": "Help Page",
            "description": descriptions
        }

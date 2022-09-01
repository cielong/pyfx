from dataclasses import dataclass

from overrides import overrides

from .view_frame import ViewFrameKeys
from .keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class ViewFrameKeyMapper(AbstractComponentKeyMapper):
    exit: str = "q"
    open_help_page: str = "?"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.exit: ViewFrameKeys.EXIT,
            self.open_help_page: ViewFrameKeys.OPEN_HELP_PAGE
        }

    @property
    @overrides
    def detailed_help(self):
        keys = [
            self.exit, self.open_help_page
        ]
        descriptions = {key: self.mapped_key[key].description for key in keys}
        return {
            "section": "Global",
            "description": descriptions
        }

from dataclasses import dataclass

from overrides import overrides

from .query_bar import QueryBarKeys
from ...keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class QueryBarKeyMapper(AbstractComponentKeyMapper):

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

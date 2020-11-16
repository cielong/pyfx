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

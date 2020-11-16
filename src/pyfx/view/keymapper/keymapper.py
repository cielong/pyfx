from dataclasses import dataclass

from ..components.autocomplete_popup.autocomplete_popup_keymapper import AutoCompletePopUpKeyMapper
from ..components.json_browser.json_browser_keymapper import JSONBrowserKeyMapper
from ..components.query_bar.query_bar_keymapper import QueryBarKeyMapper


@dataclass(frozen=True)
class KeyMapper:
    json_browser: JSONBrowserKeyMapper = JSONBrowserKeyMapper()
    query_bar: QueryBarKeyMapper = QueryBarKeyMapper()
    autocomplete_popup: AutoCompletePopUpKeyMapper = AutoCompletePopUpKeyMapper()

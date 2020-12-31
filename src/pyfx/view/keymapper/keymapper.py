from dataclasses import dataclass, field

from ..components.autocomplete_popup.autocomplete_popup_keymapper import AutoCompletePopUpKeyMapper
from ..components.json_browser.json_browser_keymapper import JSONBrowserKeyMapper
from ..components.query_bar.query_bar_keymapper import QueryBarKeyMapper


class InputFilter:

    def __init__(self, global_command_key):
        self.global_command_key = global_command_key
        self.wait_for_second_stroke = False

    def filter(self, keys, raw):
        if self.wait_for_second_stroke:
            self.wait_for_second_stroke = False
            keys[0] = self.global_command_key + " " + keys[0]
            return keys

        elif len(keys) == 1 and keys[0] == self.global_command_key:
            self.wait_for_second_stroke = True
            return

        return keys


@dataclass(frozen=True)
class KeyMapper:

    exit: str = "q"

    global_command_key: str = None
    input_filter: InputFilter = field(init=False)

    json_browser: JSONBrowserKeyMapper = JSONBrowserKeyMapper()
    query_bar: QueryBarKeyMapper = QueryBarKeyMapper()
    autocomplete_popup: AutoCompletePopUpKeyMapper = AutoCompletePopUpKeyMapper()

    def __post_init__(self):
        if self.global_command_key is not None:
            object.__setattr__(self, "input_filter", InputFilter(self.global_command_key))
        else:
            object.__setattr__(self, "input_filter", None)

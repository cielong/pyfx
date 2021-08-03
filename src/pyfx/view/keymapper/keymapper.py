from dataclasses import dataclass, field

from ..components.autocomplete_popup.autocomplete_popup_keymapper import \
    AutoCompletePopUpKeyMapper
from ..components.json_browser.json_browser_keymapper import \
    JSONBrowserKeyMapper
from ..components.query_bar.query_bar_keymapper import QueryBarKeyMapper


class InputFilter:

    def __init__(self, global_command_key):
        self.global_command_key = global_command_key
        self.wait_for_second_stroke = False

    def filter(self, keys, raw):
        if self.wait_for_second_stroke:
            self.wait_for_second_stroke = False
            combined_keys = [self.global_command_key + " " + keys[0]]
            combined_keys.extend(self.combine(keys[1:]))
            return combined_keys

        combined_keys = self.combine(keys)

        if combined_keys[-1] == self.global_command_key:
            self.wait_for_second_stroke = True
            return combined_keys[:-1]

        return combined_keys

    def combine(self, keys):
        """
        Search and combine global_command_key with the next key
        """
        combined_keys = []

        index = 0
        while index < len(keys):
            key = keys[index]

            if index == len(keys) - 1 or key != self.global_command_key:
                combined_keys.append(key)
                index += 1
                continue

            combined_keys.append(
                self.global_command_key + " " + keys[index + 1]
            )
            index += 2

        return combined_keys


@dataclass(frozen=True)
class KeyMapper:

    exit: str = "q"

    global_command_key: str = None
    input_filter: InputFilter = field(init=False)

    json_browser: JSONBrowserKeyMapper = JSONBrowserKeyMapper()
    query_bar: QueryBarKeyMapper = QueryBarKeyMapper()
    autocomplete_popup: AutoCompletePopUpKeyMapper = \
        AutoCompletePopUpKeyMapper()

    def __post_init__(self):
        object.__setattr__(
            self, "input_filter", InputFilter(self.global_command_key)
        )

"""Components that converts a keyboard input into the defined keyboard input.

Urwid only supports condition branch to handle keyboard input, as a result, all
the components and json_libs used by Pyfx have a set of predefined hard-coded
keyboard input, see
:class:`~pyfx.view.components.json_browser.json_browser.JSONBrowserKeys`.

This module is created to allow the keyboard input configurable.

The base keymapper :class:`.AbstractComponentKeyMapper` should be called before
the keyboard handling logic to convert the actual keyboard input into a fake
keyboard signal.
"""

from dataclasses import dataclass, field

from pyfx.view.components.autocomplete_popup import AutoCompletePopUpKeyMapper
from pyfx.view.components.help_popup import HelpPopUpKeyMapper
from pyfx.view.components.json_browser import JSONBrowserKeyMapper
from pyfx.view.components.query_bar import QueryBarKeyMapper


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

        if len(combined_keys) == 0:
            return combined_keys
        elif combined_keys[-1] == self.global_command_key:
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
    global_command_key: str = None
    input_filter: InputFilter = field(init=False)

    json_browser: JSONBrowserKeyMapper = JSONBrowserKeyMapper()
    query_bar: QueryBarKeyMapper = QueryBarKeyMapper()
    autocomplete_popup: AutoCompletePopUpKeyMapper = \
        AutoCompletePopUpKeyMapper()
    help_popup: HelpPopUpKeyMapper = HelpPopUpKeyMapper()

    def __post_init__(self):
        object.__setattr__(
            self, "input_filter", InputFilter(self.global_command_key)
        )

    def detailed_help(self):
        """Detailed description for all the keys."""

        # Each item in the list falls into the following structure,
        # {
        #    "section": <section_title>,
        #    "description": [(key_stroke, key_description)...]
        # }
        description = [
            self.json_browser.detailed_help,
            self.query_bar.detailed_help,
            self.autocomplete_popup.detailed_help,
            self.help_popup.detailed_help
        ]

        return description

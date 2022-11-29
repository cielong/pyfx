"""Module of general text input classes, such as the file name to save."""
from dataclasses import dataclass
from enum import Enum

import urwid
from overrides import overrides

from pyfx.view.components.abstract_component_keys import BaseComponentKeyMapper
from pyfx.view.components.abstract_component_keys import KeyDefinition


class InputBarKeys(KeyDefinition, Enum):
    """Enums for all the available keys defined in InputBar."""

    CONFIRM = "enter", "Finish the current input."
    CANCEL = "esc", "Cancel input."


@dataclass(frozen=True)
class InputBarKeyMapper(BaseComponentKeyMapper):
    confirm: str = "enter"
    cancel: str = "esc"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.confirm: InputBarKeys.CONFIRM,
            self.cancel: InputBarKeys.CANCEL
        }

    @property
    @overrides
    def short_help(self):
        return [f"CONFIRM: {self.confirm}",
                f"CANCEL: {self.cancel}"]

    @property
    @overrides
    def detailed_help(self):
        keys = [self.confirm, self.cancel]
        descriptions = {key: self.mapped_key[key].description for key in keys}
        return {
            "section": "Save Bar",
            "description": descriptions
        }


class InputBar(urwid.WidgetWrap):
    def __init__(self, keymapper, client, mediator, message):
        self._keymapper = keymapper
        self._client = client
        self._mediator = mediator
        self._message = message
        super().__init__(urwid.Edit(message))

    def help_message(self):
        return self._keymapper.short_help

    @overrides
    def keypress(self, size, original_key):
        key = self._keymapper.key(original_key)
        key = super().keypress(size, key)

        if key is None:
            return None

        if key == InputBarKeys.CONFIRM.key:
            file_path = self._w.text[len(self._message):]
            save_result = self._client.invoke("save", file_path)

            if not save_result:
                self._mediator.notify("input_bar", "update", "warning_bar",
                                      "Failed to save the current json data "
                                      f"into file {file_path}.")
                self._mediator.notify("input_bar", "show", "view_frame",
                                      "warning_bar", True)
            else:
                self._mediator.notify("input_bar", "update", "warning_bar",
                                      "Saved the current data successfully.")
                self._mediator.notify("input_bar", "show", "view_frame",
                                      "json_browser", True)
            return None

        if key == InputBarKeys.CANCEL.key:
            self._mediator.notify("query_bar", "show", "view_frame",
                                  "json_browser", True)
            return None

        return original_key

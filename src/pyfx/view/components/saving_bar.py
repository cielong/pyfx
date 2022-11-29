"""Module of general text input classes, such as the file name to save."""
from dataclasses import dataclass
from enum import Enum

import urwid
from overrides import overrides

from pyfx.view.components.abstract_component_keys import BaseComponentKeyMapper
from pyfx.view.components.abstract_component_keys import KeyDefinition


class SavingBarKeys(KeyDefinition, Enum):
    """Enums for all the available keys defined in InputBar."""

    SAVE = "enter", "Finish the current input."
    CANCEL = "esc", "Cancel input."


@dataclass(frozen=True)
class SavingBarKeyMapper(BaseComponentKeyMapper):
    save: str = "enter"
    cancel: str = "esc"

    @property
    @overrides
    def mapped_key(self):
        return {
            self.save: SavingBarKeys.SAVE,
            self.cancel: SavingBarKeys.CANCEL
        }

    @property
    @overrides
    def short_help(self):
        return [f"CONFIRM: {self.save}",
                f"CANCEL: {self.cancel}"]

    @property
    @overrides
    def detailed_help(self):
        keys = [self.save, self.cancel]
        descriptions = {key: self.mapped_key[key].description for key in keys}
        return {
            "section": "Saving Bar",
            "description": descriptions
        }


class SavingBar(urwid.WidgetWrap):
    PREFIX = "Save the current view into file: "

    def __init__(self, keymapper, client, mediator):
        self._keymapper = keymapper
        self._client = client
        self._mediator = mediator
        super().__init__(urwid.Edit(SavingBar.PREFIX))

    def help_message(self):
        return self._keymapper.short_help

    @overrides
    def keypress(self, size, original_key):
        key = self._keymapper.key(original_key)
        key = super().keypress(size, key)

        if key is None:
            return None

        if key == SavingBarKeys.SAVE.key:
            file_path = self._w.text[len(SavingBar.PREFIX):]
            save_result = self._client.invoke("save", file_path)

            if not save_result:
                self._mediator.notify("saving_bar", "update", "warning_bar",
                                      "Failed to save the current json data "
                                      f"into file {file_path}.")
                self._mediator.notify("saving_bar", "show", "view_frame",
                                      "warning_bar", False)
            else:
                self._mediator.notify("saving_bar", "update", "warning_bar",
                                      "Saved the current data successfully.")
                self._mediator.notify("saving_bar", "show", "view_frame",
                                      "warning_bar", False)
                self._mediator.notify("input_bar", "show", "view_frame",
                                      "json_browser", True)
            return None

        if key == SavingBarKeys.CANCEL.key:
            # Hide the saving bar and then reset the text in saving bar to
            # its original prefix
            self._mediator.notify("saving_bar", "show", "view_frame",
                                  "query_bar", False)
            self._w.set_text(SavingBar.PREFIX)
            self._mediator.notify("saving_bar", "show", "view_frame",
                                  "json_browser", True)
            return None

        return original_key

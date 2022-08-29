from enum import Enum

import urwid
from overrides import overrides

from ...common import SelectableText
from ...keymapper import KeyDefinition


class HelpPopUpKeys(KeyDefinition, Enum):
    CURSOR_UP = "up", "Move cursor up one line in the help."
    CURSOR_DOWN = "down", "Move cursor down one line in the help."
    EXIT = "esc", "Close help page."

    @classmethod
    def list(cls):
        return list(map(lambda k: k.key, cls))


class HelpPopUp(urwid.WidgetWrap):
    """
    Help popups for documentation.
    """

    def __init__(self, documentation, mediator, keymapper):
        self._documentation = documentation
        self._mediator = mediator
        self._keymapper = keymapper
        super().__init__(self._load_widget())

    @overrides
    def pack(self, size, focus=False):
        """
        Compute the minimum (col, row) size needed for rendering the options.
        """
        max_rows = 15
        max_cols = 40

        total_rows = 0
        for section in self._documentation:
            # one row for section title
            total_rows += 1
            for key, description in section["description"].items():
                max_cols = max(max_cols, len(key) + 2 + len(description))
                total_rows += 1
            # blank line after each section
            total_rows += 1

        max_rows = min(max(max_rows, total_rows), 25)
        max_cols = min(max_cols, 80)
        return max_cols, max_rows

    def _load_widget(self):
        widgets = []
        for section in self._documentation:
            for section_widget in self.__section_widget(section):
                widgets.append(urwid.AttrMap(
                    section_widget, None, "help.popup.focused"
                ))
        listbox = urwid.ListBox(urwid.SimpleListWalker(widgets))
        frame = urwid.Frame(listbox, footer=urwid.Text("Press esc to close."))
        lined_frame = urwid.LineBox(frame)
        return urwid.AttrMap(lined_frame, "help.popup")

    def __section_widget(self, section):
        # section title
        section_title = urwid.Text(('title', section["section"]))
        # section details
        max_width = max([len(key) for key in section["description"]])
        section_details = [
            urwid.Columns([
                (max_width + 2, SelectableText(key)),
                SelectableText(description),
            ])
            for key, description in section["description"].items()]

        return [section_title, *section_details]

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == HelpPopUpKeys.EXIT.key:
            self._mediator.notify("help_popup", "close_pop_up")
            return

        return key

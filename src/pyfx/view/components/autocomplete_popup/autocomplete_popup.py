from enum import Enum

import urwid
from overrides import overrides

from ...common import SelectableText
from ...keymapper import KeyDefinition


class AutoCompletePopUpKeys(KeyDefinition, Enum):
    CURSOR_UP = "up", "Move cursor up one line in the option list."
    CURSOR_DOWN = "down", "Move cursor down one line in the option list."
    SELECT = "enter", "Select the current option."
    CANCEL = "esc", "Cancel auto-completion."


class AutoCompletePopUp(urwid.WidgetWrap):
    """Auto-complete popups for autocomplete suggestions of query input.
    """

    # predefined constants to constrain pop up window size
    MAX_HEIGHT = 5

    def __init__(self, mediator, keymapper, prefix,
                 options, is_partial_complete):
        self._mediator = mediator
        self._keymapper = keymapper

        self._prefix = prefix
        self._options = options
        self._partial_complete = is_partial_complete
        super().__init__(self._load_widget())

    @overrides
    def pack(self, size, focus=False):
        """
        Compute the minimum (col, row) size needed for rendering the options.

        :param size: the size of the pop up launcher
        :type size: (int, int)
        :param focus: focus on the popup or not
        :type focus: bool
        :return: (min_col, min_row) of the pop up
        """
        max_width = max([len(c) for c in self._options])
        max_height = min(len(self._options), AutoCompletePopUp.MAX_HEIGHT)
        return max_width, max_height

    def _load_widget(self):
        widgets = [
            urwid.AttrMap(
                SelectableText(o, wrap='ellipsis'), None, 'autocomplete.focused'
            )
            for o in self._options
        ]
        listbox = urwid.ListBox(urwid.SimpleListWalker(widgets))
        return urwid.AttrMap(listbox, 'autocomplete')

    def _get_focus_text(self):
        _, position = self._w.original_widget.get_focus()
        return self._options[position]

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key is None:
            return None

        if key == AutoCompletePopUpKeys.SELECT.key:
            option = self._get_focus_text()[len(self._prefix):]
            self._mediator.notify("autocomplete", "close_pop_up", "view_frame")
            self._mediator.notify("autocomplete", "select_complete_option",
                                  "query_bar", option, self._partial_complete)
            return None

        elif key == AutoCompletePopUpKeys.CANCEL.key:
            self._mediator.notify("autocomplete", "close_pop_up", "view_frame")
            return None

        # forward key to the query window if not handled by auto-complete
        if key is not None:
            result = self._mediator.notify("autocomplete", "pass_keypress",
                                           "query_bar", key)
            if result is None:
                # handled by query bar
                return None

        return key

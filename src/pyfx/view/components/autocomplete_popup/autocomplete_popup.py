from enum import Enum

import urwid
from overrides import overrides

from ...common import SelectableText


class AutoCompletePopUpKeys(Enum):
    CURSOR_UP = "up"
    CURSOR_DOWN = "down"
    SELECT = "enter"
    CANCEL = "esc"

    @classmethod
    def list(cls):
        return list(map(lambda k: k.value, cls))


class AutoCompletePopUp(urwid.WidgetWrap):
    """
    Auto-complete popups for autocomplete suggestions of query input.
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
                SelectableText(o, wrap='ellipsis'), None, 'popup.focused'
            )
            for o in self._options
        ]
        listbox = urwid.ListBox(urwid.SimpleListWalker(widgets))
        return urwid.AttrMap(listbox, 'popup')

    def _get_focus_text(self):
        _, position = self._w.original_widget.get_focus()
        return self._options[position]

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == AutoCompletePopUpKeys.SELECT.value:
            option = self._get_focus_text()[len(self._prefix):]
            self._mediator.notify("close_pop_up", "autocomplete")
            self._mediator.notify(
                "select_complete_option",
                "autocomplete",
                option,
                self._partial_complete
            )
            return

        elif key == AutoCompletePopUpKeys.CANCEL.value:
            self._mediator.notify("close_pop_up", "autocomplete")
            return

        elif key in AutoCompletePopUpKeys.list():
            # some keys are handled by super().keypress(self, key) but filter
            # out here
            return

        # forward key to the query window if not handled by auto-complete
        if key is not None:
            result = self._mediator.notify("keypress", "autocomplete", key)
            if len(result) == 1 and result[0] is None:
                # handled by query bar
                return

        return key

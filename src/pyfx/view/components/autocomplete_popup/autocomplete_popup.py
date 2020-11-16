from enum import Enum

import urwid
from overrides import overrides

from ...common import SelectableText


class AutoCompletePopUpKeys(Enum):
    CURSOR_UP = "up"
    CURSOR_DOWN = "down"
    SELECT = "enter"
    CANCEL = "esc"


class AutoCompletePopUp(urwid.WidgetWrap):
    """
    Auto-complete popups for autocomplete suggestions of query input.
    """

    # predefined constants to constrain pop up window size
    MAX_HEIGHT = 5

    def __init__(self, controller, keymapper, popup_launcher, query_window, prefix, options):
        self._popup_launcher = popup_launcher
        self._query_window = query_window
        self._controller = controller
        self._keymapper = keymapper

        self._prefix = prefix
        self._options = options
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
        widgets = [urwid.AttrWrap(SelectableText(o, wrap='ellipsis'), None, 'focus')
                   for o in self._options]
        listbox = urwid.ListBox(urwid.SimpleListWalker(widgets))
        return urwid.AttrWrap(listbox, 'popup')

    def _get_focus_text(self):
        _, position = self._w.get_focus()
        return self._options[position]

    def _update_query(self):
        option = self._get_focus_text()
        option = option[len(self._prefix):]
        if self._query_window.get_text().endswith(']'):
            # mixed style needs to be taken care
            option = '.' + option
        self._query_window.insert_text(option)

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == AutoCompletePopUpKeys.SELECT.value:
            self._update_query()
            self._popup_launcher.close_pop_up()
            self._controller.query(self._query_window.get_text())
            return None

        elif key == AutoCompletePopUpKeys.CANCEL.value:
            self._popup_launcher.close_pop_up()
            return None

        elif key is not None:
            # forward key to the query window if not handled by auto-complete
            self._popup_launcher.close_pop_up()
            key = self._query_window.keypress_internal(key)

        return key

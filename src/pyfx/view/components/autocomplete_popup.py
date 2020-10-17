import urwid
from overrides import overrides

from ..common import SelectableText


class AutoCompletePopUp(urwid.WidgetWrap):
    """
    Auto-complete popups for autocomplete suggestions of query input.
    """

    # predefined constants to constrain pop up window size
    MAX_HEIGHT = 5

    def __init__(self, popup_launcher, controller, query_window, prefix, options):
        self._popup_launcher = popup_launcher
        self._query_window = query_window
        self._controller = controller
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

    @overrides
    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == 'enter':
            option = self._get_focus_text()[len(self._prefix):]
            self._popup_launcher.close_pop_up()
            self._controller.update_complete(option)
            return None
        elif key in ('esc', 'ctrl g'):
            self._popup_launcher.close_pop_up()
            return None
        elif key is not None:
            # forward key to the query window if not handled by auto-complete
            self._popup_launcher.close_pop_up()
            key = self._query_window.keypress_internal(key)
        return key

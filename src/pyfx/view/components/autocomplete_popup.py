import urwid
from overrides import overrides

from ..common import SelectableText


class AutoCompletePopUp(urwid.WidgetWrap):
    """
    Autocomplete popup window for autocomplete suggestions in query window.
    """

    # predefined constants to constrain pop up window size
    MAX_HEIGHT = 5

    def __init__(self, popup_launcher, controller, query_window, options):
        self._popup_launcher = popup_launcher
        self._query_window = query_window
        self._controller = controller
        self._options = options
        super().__init__(self._load_widget())

    @overrides
    def pack(self, size, focus=False):
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
            option = self._get_focus_text()
            self._popup_launcher.close_pop_up()
            self._controller.update_complete(option)
        elif key in ('esc', 'ctrl g'):
            self._popup_launcher.close_pop_up()
            return
        # forward key
        self._popup_launcher.close_pop_up()
        key = self._query_window.keypress_internal(key)
        return key

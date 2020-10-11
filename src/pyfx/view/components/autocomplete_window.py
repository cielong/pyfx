import urwid

from ..common import SelectableText


class AutoCompleteWindow(urwid.WidgetWrap):
    """
    Autocomplete popup window for autocomplete suggestions in query window.
    """

    # predefined constants to constrain pop up window size
    MAX_HEIGHT = 5
    MIN_WIDTH = 4

    def __init__(self, view, size, options: list):
        self._view = view
        self._options = options
        (self.width, self.height) = self._calculate_max_size(size)
        self._inner_widget = self._load_inner_widget()
        super().__init__(self._load_widget())

    def _calculate_max_size(self, size):
        width, height = map(lambda num: 3 * num // 4, size)

        if len(self._options) == 0:
            max_options_width = width
        else:
            max_options_width = max([len(o) for o in self._options])

        width = max(AutoCompleteWindow.MIN_WIDTH, min(width, max_options_width))
        height = min(AutoCompleteWindow.MAX_HEIGHT, min(height, len(self._options)))

        return width, height

    def _load_inner_widget(self):
        option_widgets = []
        for o in self._options:
            option_widgets.append(SelectableText(o, wrap='ellipsis'))
        return option_widgets

    def _load_widget(self):
        decorated_inner_widget = [
            urwid.AttrWrap(urwid.Padding(w, width=self.width)) for w in self._inner_widget
        ]
        listbox = urwid.ListBox(urwid.SimpleListWalker(decorated_inner_widget))
        return urwid.AttrWrap(listbox, 'body')

    def _get_focus_text(self):
        _, position = self._listbox.get_focus()
        text, _ = self._inner_widget[position].get_text()
        return text

    def exit(self):
        self._view.exit_window(self)

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == 'enter':
            self._view.controller.query(self._get_focus_text())
        elif key == 'esc':
            self.exit()
        return key

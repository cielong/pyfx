import urwid

from pyfx.view.common.selectable_text import SelectableText


class AutoCompleteWindow(urwid.WidgetWrap):
    # predefined constants to constrain pop up window size
    MAX_HEIGHT = 5
    MIN_WIDTH = 4

    def __init__(self, view, size, options: list):
        self._view = view
        self._options = options
        (self.width, self.height) = self._calculate_max_size(size)
        self._listbox = self._load_inner_widget()
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
            inner_widget = urwid.Padding(
                SelectableText(o, wrap='ellipsis'),
                width=self.width,
                min_width=self.width
            )
            option_widgets.append(urwid.AttrWrap(inner_widget, None, 'focus'))

        return urwid.ListBox(urwid.SimpleListWalker(option_widgets))

    def _load_widget(self):
        linebox = urwid.LineBox(self._listbox)
        return urwid.AttrWrap(linebox, 'body')

    def _get_focus_text(self):
        focus, _ = self._listbox.get_focus()
        padding_widget = focus._get_original_widget()
        text, _ = padding_widget._get_original_widget().get_text()
        return text

    def exit(self):
        self._invalidate()
        self._view.exit_window(self)

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == 'enter':
            self._invalidate()
            self._view.controller.apply_autocomplete(self._get_focus_text())
        elif key == 'esc':
            self.exit()
        return key

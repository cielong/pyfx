from enum import Enum

import urwid


class MainWindow(urwid.Frame):
    """ customized keypress for main window """

    class _FocusArea(Enum):
        BODY = "body"
        FOOTER = "footer"

    def __init__(self, view_window, query_window, help_window, help_details_window):
        self._view_window = view_window
        self._query_window = query_window
        self._help_window = help_window
        self._help_details_window = help_details_window
        super().__init__(self._view_window, footer=self._help_window)

    def refresh_view(self, data):
        self._view_window.set_data(data)

    def enter_help_details_window(self):
        self.set_body(self._help_details_window)

    def enter_query_window(self):
        self._query_window.setup()
        self.set_footer(self._query_window)
        self.set_focus(MainWindow._FocusArea.FOOTER.value)

    def exit(self):
        if self.get_footer() == self._query_window:
            self._query_window.reset()
            self.set_footer(self._help_window)
            self.set_focus(MainWindow._FocusArea.BODY.value)
        elif self.get_body() == self._help_details_window:
            self.set_body(self._view_window)

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == '?':
            self.enter_help_details_window()
        elif key == '.':
            self.enter_query_window()
        elif key == 'esc':
            self.exit()
        return key

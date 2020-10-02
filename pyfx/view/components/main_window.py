from enum import Enum

import urwid

from pyfx.view.components.help_details_window import HelpDetailsWindow
from pyfx.view.components.help_window import HelpWindow
from pyfx.view.components.query_window import QueryWindow
from pyfx.view.components.view_window import ViewWindow


class MainWindow(urwid.Frame):
    """ customized keypress for main window """

    class _FocusArea(Enum):
        BODY = "body"
        FOOTER = "footer"

    def __init__(self, view, data):
        self._view = view
        self._view_window = ViewWindow(data)
        self._query_window = QueryWindow(self._view.controller.autocomplete)
        self._help_window = HelpWindow()
        self._help_details_window = HelpDetailsWindow()
        super().__init__(self._view_window, footer=self._help_window)

    def refresh_view(self, data):
        self._view_window.set_data(data)

    def enter_help_details_window(self):
        self.set_body(self._help_details_window)

    def enter_query_window(self, size):
        self._query_window.setup(size)
        self.set_footer(self._query_window)
        self.set_focus(MainWindow._FocusArea.FOOTER.value)

    def get_query_text(self):
        return self._query_window.get_edit_text()

    def apply_autocomplete(self, text):
        self._query_window.set_edit_text(text)

    def exit(self, window=None):
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
            self.enter_query_window(size)
        elif key == 'esc':
            self.exit()
        return key

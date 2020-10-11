from enum import Enum

import urwid

from .help_details_window import HelpDetailsWindow
from .help_window import HelpWindow
from .query_window import QueryWindow
from .view_window import ViewWindow


class MainWindow(urwid.Frame):
    """
    Main UI for pyfx
    """

    def __init__(self, view, data):
        self._view = view
        self._view_window = ViewWindow(data)
        self._query_window = QueryWindow(self._view.controller)
        self._help_window = HelpWindow()
        self._help_details_window = HelpDetailsWindow()
        super().__init__(self._view_window, footer=self._help_window)

    def refresh_view(self, data):
        self._view_window.set_top_node(data)

    def change_focus(self, area):
        self.focus_position = area.value

    def enter_help_details_window(self):
        self._body = self._help_details_window

    def enter_query_window(self, size):
        self._query_window.setup(size)
        self._footer = self._query_window
        self.change_focus(FocusArea.FOOTER)

    def get_query_text(self):
        return self._query_window.get_text()

    def update_query_text(self, text):
        self._query_window.insert_edit_text(text)

    def exit(self, window=None):
        if self.get_footer() == self._query_window:
            self._query_window.reset()
            self._footer = self._help_window
            self.change_focus(FocusArea.BODY)
        elif self.get_body() == self._help_details_window:
            self._body = self._view_window

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == '?':
            self.enter_help_details_window()
        elif key == '.':
            self.enter_query_window(size)
        elif key == 'esc':
            self.exit()
        return key


class FocusArea(Enum):
    """
    Enum for focus area in Main Window
    """
    BODY = "body"
    FOOTER = "footer"

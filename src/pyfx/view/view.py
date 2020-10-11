import traceback

import urwid

from .components.autocomplete_window import AutoCompleteWindow
from .components import MainWindow, FocusArea


class View:
    """
    UI entry point for pyfx, which will be used to also manages the UI thread

    .. data:`palette`
       The current theme defined in `pyfx`.
    """

    palette = [
        ('body', 'black', 'light gray'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('head', 'yellow', 'black', 'standout'),
        ('foot', 'light gray', 'black'),
        ('key', 'light cyan', 'black', 'underline'),
        ('title', 'white', 'black', 'bold'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
    ]

    def __init__(self, controller):
        """
        :param controller: The controller/presenter used in `pyfx` to initialize data change.
        :type controller: :py:class:`pyfx.core.Controller`
        """
        self._controller = controller
        self._data = None
        self._main_window = MainWindow(self, self._data)
        self._screen = urwid.raw_display.Screen()
        self._loop = None

    @property
    def controller(self):
        return self._controller

    def run(self, data):
        """
        To start the :py:class:`urwid.MainLoop`.

        :param data: the current JSON data
        :return:
        """
        self._main_window.refresh_view(data)
        self._loop = urwid.MainLoop(
            self._main_window, self.palette,
            screen=self._screen, unhandled_input=self.unhandled_input
        )

        # noinspection PyBroadException
        try:
            self._loop.run()
        except Exception:
            traceback.print_exc()
            self._screen.clear()

    def enter_autocomplete_popup(self, size, widget, options):
        autocomplete_window = AutoCompleteWindow(self, size, options)
        cur_coords = self._main_window.get_cursor_coords(size)
        if cur_coords is None:
            # TODO: should always get valid coordinates and raise if empty
            # raise ExitMainLoop(Exception("Cannot get current cursor coordinates."))
            return
        (cur_col, cur_row) = cur_coords
        self._loop.widget = urwid.Overlay(
            autocomplete_window,
            self._main_window,
            align='left',
            valign='bottom',
            width=autocomplete_window.width + 2,
            height=autocomplete_window.height + 2,
            left=cur_col + 1,
            bottom=1
        )

    def get_query_text(self):
        return self._main_window.get_query_text()

    def refresh(self, data):
        self._main_window.refresh_view(data)
        self._main_window.change_focus(FocusArea.BODY)

    def exit_window(self, window):
        if isinstance(window, AutoCompleteWindow):
            self._loop.widget = self._main_window
        else:
            self._main_window.exit(window)

    def exit(self, exception=None):
        if not self._loop:
            return

        if exception:
            raise urwid.ExitMainLoop(exception)
        raise urwid.ExitMainLoop()

    def unhandled_input(self, k):
        if k in ('q', 'Q'):
            self.exit()

import traceback

import urwid

from pyfx.view.json_lib.json_listbox import JSONListBox
from pyfx.view.json_lib.json_listwalker import JSONListWalker
from pyfx.view.json_lib.models.node_factory import NodeFactory
from pyfx.view.windows.help_details_window import HelpDetailsWindow
from pyfx.view.windows.help_window import HelpWindow
from pyfx.view.windows.main_window import MainWindow
from pyfx.view.windows.query_window import QueryWindow
from pyfx.view.windows.view_window import ViewWindow


class View:
    """ UI entry point for pyfx """

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

    def __init__(self, controller: "Controller"):
        self._controller = controller
        self._data = None
        self._main_window = MainWindow(
            ViewWindow(self._data), QueryWindow(self._controller.autocomplete),
            HelpWindow(), HelpDetailsWindow()
        )
        self._screen = urwid.raw_display.Screen()
        self._loop = None

    def run(self, data):
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

    def pop_up_autocomplete_options(self, options):
        pass

    def exit(self, exception=None):
        if not self._loop:
            return

        if exception:
            raise urwid.ExitMainLoop(exception)
        raise urwid.ExitMainLoop()

    def unhandled_input(self, k):
        if k in ('q', 'Q'):
            self.exit()

import urwid
from loguru import logger

from .components import AutoCompletePopUp
from .components import HelpBar
from .components import JSONBrowser
from .components import QueryBar
from .keymapper import KeyMapperConfigurationParser
from .view_frame import FocusArea
from .view_frame import ViewFrame


class View:
    """
    pyfx UI entry point.

    It manages the UI thread and switches views between components with keypress.

    .. data:`palette`
       The current theme defined in `pyfx`.
    """

    palette = [
        # normal mapping
        ('body', 'white', 'default'),
        ('foot', 'light gray', 'default'),
        ('key', 'dark cyan', 'default'),
        ('title', 'white', 'default', 'bold'),
        # focused mapping
        ('focus', 'light gray', 'dark blue', 'standout')
    ]

    def __init__(self, controller, config):
        """
        :param controller: The controller/presenter used in `pyfx` to initialize data change.
        :type controller: :py:class:`pyfx.core.Controller`
        """
        self._controller = controller
        self._config = config

        self._data = None
        self._keymapper = KeyMapperConfigurationParser.create_keymapper(self._config.keymap)

        # different window components
        self._view_window = JSONBrowser(self, self._keymapper.json_browser, self._data)
        self._query_window = QueryBar(self, controller, self._keymapper.query_bar)
        self._help_window = HelpBar(self)

        # view frame
        def popup_factory(popup_launcher, query_bar, prefix, options):
            return AutoCompletePopUp(controller, self._keymapper.autocomplete_popup, popup_launcher, query_bar,
                                     prefix, options)
        self._frame = ViewFrame(self._view_window, self._help_window, popup_factory)
        self._screen = None
        self._loop = None

    def run(self, data):
        """
        To start the :py:class:`urwid.MainLoop`.

        :param data: the current JSON data
        :return:
        """
        self._view_window.set_top_node(data)
        self._screen = urwid.raw_display.Screen(input=open('/dev/tty'))
        self._loop = urwid.MainLoop(
            self._frame, self.palette,
            pop_ups=True, screen=self._screen,
            unhandled_input=self.unhandled_input
        )

        # noinspection PyBroadException
        try:
            self._loop.run()
        except Exception as e:
            logger.opt(exception=True).error("Unknown exception encountered, exit with {}", e)
            self._screen.clear()

    def size(self):
        return self._screen.get_cols_rows()

    def close_autocomplete_popup(self):
        if self._frame.pop_up_widget:
            self._frame.close_pop_up()

    def open_autocomplete_popup(self, prefix, options):
        self._frame.open_pop_up(widget=self._query_window, prefix=prefix, options=options)

    def update_complete(self, text):
        self._query_window.reset()
        self._query_window.insert_text(text)
        self._query_window.setup()

    def enter_query_window(self):
        self._query_window.setup()
        self._frame.change_widget(self._query_window, FocusArea.FOOTER)
        self._frame.change_focus(FocusArea.FOOTER)

    def exit_query_window(self):
        self._frame.change_widget(self._help_window, FocusArea.FOOTER)
        self._frame.change_focus(FocusArea.BODY)

    def enter_view_window(self):
        self._frame.change_focus(FocusArea.BODY)

    def get_query(self):
        return self._query_window.get_text()

    def refresh(self, data):
        self._view_window.set_top_node(data)

    def exit(self, exception=None):
        if not self._loop:
            return
        if exception:
            raise urwid.ExitMainLoop(exception)
        raise urwid.ExitMainLoop()

    def unhandled_input(self, k):
        if k in ('q', 'Q'):
            self.exit()

import urwid
from loguru import logger

from .keymapper import create_keymapper
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
        ('title', 'white', 'default', 'bold'),
        ('popup', 'black', 'light cyan'),
        ('json.key', 'light blue', 'default'),
        ('json.string', 'light green', 'default'),
        ('json.integer', 'light cyan', 'default'),
        ('json.numeric', 'light cyan', 'default'),
        ('json.bool', 'yellow', 'default'),
        ('json.null', 'light red', 'default'),
        # focused mapping
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('popup.focused', 'white', 'dark magenta', 'standout'),
        ('json.focused', 'light gray', 'dark blue', 'standout')
    ]

    def __init__(self, controller, config):
        """
        :param controller: The controller/presenter used in `pyfx` to initialize data change.
        :type controller: :py:class:`pyfx.core.Controller`
        """
        self._controller = controller
        self._config = config
        self._frame = ViewFrame(self, controller, create_keymapper(self._config.keymap))

        self._screen = None
        self._loop = None

    def run(self, data):
        """
        To start the :py:class:`urwid.MainLoop`.

        :param data: the current JSON data
        :return:
        """
        self._frame.set_data(data)
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

    def exit(self, exception=None):
        if not self._loop:
            return
        if exception:
            raise urwid.ExitMainLoop(exception)
        raise urwid.ExitMainLoop()

    def unhandled_input(self, k):
        if k in ('q', 'Q'):
            self.exit()

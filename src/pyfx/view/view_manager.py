import sys

import urwid
from loguru import logger

from .view_frame import ViewFrame


class View:
    """
    pyfx UI entry point.

    It manages the UI thread and switches views between components with
    keypress.

    .. data:`palette`
       The current theme defined in `pyfx`.
    """

    def __init__(self, config, client):
        """
        """
        self._config = config
        self._frame = ViewFrame(client, self, self._config.keymap.mapping)

        self._input_filter = self._config.keymap.mapping.input_filter

        self._screen = None
        self._loop = None

    def run(self, data):
        """
        To start the :py:class:`urwid.MainLoop`.

        :param data: the current JSON data
        :return:
        """
        self._frame.set_data(data)
        # Specify the `input` to force Screen reload the value for sys.stdin
        # as sys.stdin may be redirected. E.g., when pyfx is using with pipe,
        # we replaced the sys.stdin at the CLI level
        self._screen = urwid.raw_display.Screen(input=sys.stdin)
        # noinspection PyBroadException
        try:
            # this is to turn off control for SIGTERM while in pyfx
            self._screen.tty_signal_keys('undefined', 'undefined', 'undefined',
                                         'undefined', 'undefined')
        except Exception:
            # avoid potential error during e2e test
            pass
        self._loop = urwid.MainLoop(
            self._frame,
            self._config.appearance.color_scheme,
            pop_ups=True,
            screen=self._screen,
            input_filter=self._input_filter.filter,
            unhandled_input=self.unhandled_input
        )

        # noinspection PyBroadException
        try:
            self._loop.run()
        except urwid.ExitMainLoop:
            # urwid exit normally
            pass
        except Exception as e:
            logger.opt(exception=True).\
                error("Unknown exception encountered in view_manager.run, "
                      "exit with {}", e)
            # re-raise the exception
            raise e
        finally:
            self._screen.clear()

    def process_input(self, data, keys):
        """
        Test-used only to process a list of keypress
        """
        self._frame.set_data(data)
        self._screen = urwid.raw_display.Screen()
        self._loop = urwid.MainLoop(
            self._frame,
            self._config.appearance.color_scheme,
            pop_ups=True,
            screen=self._screen,
            input_filter=self._input_filter.filter,
            unhandled_input=self.unhandled_input
        )

        try:
            for index, key in enumerate(keys):
                # work around for urwid.MainLoop#process_input does not apply
                # input filter
                key = self._loop.input_filter([key], None)
                if len(key) >= 1 and (not self._loop.process_input(key)):
                    return False, f"keys[{index}]: {key} is not handled"
        except urwid.ExitMainLoop:
            pass
        finally:
            self._screen.clear()
        return True, ""

    def size(self):
        return self._screen.get_cols_rows()

    def exit(self, exception=None):
        if not self._loop:
            return
        if exception:
            raise urwid.ExitMainLoop(exception)
        raise urwid.ExitMainLoop()

    def unhandled_input(self, k):
        if k == self._config.keymap.mapping.exit:
            self.exit()

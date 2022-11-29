import urwid
from loguru import logger


class View:
    """
    pyfx UI entry point.

    It manages the UI thread and switches views between components with
    keypress.

    .. data:`palette`
       The current theme defined in `pyfx`.
    """

    def __init__(self, palette, input_filter, screen, frame):
        self._frame = frame
        self._screen = screen
        self._input_filter = input_filter
        self._loop = urwid.MainLoop(self._frame, palette, pop_ups=True,
                                    screen=self._screen,
                                    input_filter=self._input_filter.filter)

    def run(self):
        """
        To start the :py:class:`urwid.MainLoop`.
        """
        # noinspection PyBroadException
        try:
            self._loop.run()
        except urwid.ExitMainLoop:
            # urwid exit normally
            pass
        except Exception as e:
            logger.opt(exception=True). \
                error("Unknown exception encountered in view_manager.run, "
                      "exit with {}", e)
            # re-raise the exception
            raise e
        finally:
            self._screen.clear()

    def process_input(self, keys):
        """
        Test-used only to process a list of keypress
        """
        try:
            for index, key in enumerate(keys):
                # work around for urwid.MainLoop#process_input does not apply
                # input filter
                key = self._loop.input_filter([key], None)

                if len(key) == 0:
                    continue
                elif self._loop.process_input(key):
                    continue

                return False, f"keys[{index}]: {key} is not handled"
        except urwid.ExitMainLoop:
            pass
        finally:
            self._screen.clear()
        return True, ""

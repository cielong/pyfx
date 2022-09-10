"""Pyfx app, the main entry point of pyfx library."""
import sys
from concurrent.futures.thread import ThreadPoolExecutor

import urwid
from loguru import logger

from .config import parse
from .error import PyfxException
from .model import Model
from .service.client import Client
from .service.dispatcher import Dispatcher
from .view import View
from .view.components import JSONBrowser, QueryBar, HelpBar, AutoCompletePopUp
from .view.components.help.help_popup import HelpPopUp
from .view.json_lib.json_node_factory import JSONNodeFactory
from .view.view_frame import ViewFrame
from .view.view_mediator import ViewMediator


class PyfxApp:
    """Pyfx app, the main entry point of pyfx library."""

    def __init__(self, data, config=None, debug_mode=False):
        """PyfxApp Constructor.

        Args:
            data: The actual data to be visualized.
                While the data is supposed to be in the JSON format, this
                requirement is not enforced and validated here.
            config: The path of the configuration file.
                `None` asks Pyfx to search the config file in pre-defined locations.
            debug_mode: A flag to indicate whether debug logging is enabled or not.
        """
        self.__init_logger(debug_mode)

        self._config = self.__read_config(config)

        self._data = data
        self._keymapper = self._config.view.keymap.mapping

        # backend part
        self._dispatcher = Dispatcher()
        # model
        self._model = Model(self._data)
        self._dispatcher.register("query", self._model.query)
        self._dispatcher.register("complete", self._model.complete)

        # UI part
        self._thread_pool_executor = ThreadPoolExecutor()
        self._client = Client(self._dispatcher, self._thread_pool_executor)
        # Specify the `input` to force Screen reload the value for sys.stdin
        # as sys.stdin may be redirected. E.g., when pyfx is using with pipe,
        # we replaced the sys.stdin at the CLI level
        self._screen = self.__create_screen()
        self._mediator = ViewMediator()

        # view_frame bodies
        self._node_factory = JSONNodeFactory()
        self._json_browser = JSONBrowser(self._node_factory, self._mediator,
                                         self._keymapper.json_browser)
        self._mediator.register("json_browser", "refresh_view",
                                self._json_browser.refresh_view)

        # view_frame footers
        self._help_bar = HelpBar(self.__short_help())
        self._query_bar = QueryBar(self._mediator, self._client,
                                   self._keymapper.query_bar)
        self._mediator.register("query_bar", "select_complete_option",
                                self._query_bar.insert_text)
        self._mediator.register("query_bar", "pass_keypress",
                                self._query_bar.pass_keypress)

        # pop up factories
        def autocomplete_factory(*args, **kwargs):
            def get_autocomplete_popup_params(original_widget, pop_up_widget,
                                              size):
                cur_col, _ = original_widget.get_cursor_coords(size)
                popup_max_col, popup_max_row = pop_up_widget.pack(size)
                max_col, max_row = size
                footer_rows = original_widget.footer.rows((max_col,))
                return {
                    'left': cur_col,
                    'top': max_row - popup_max_row - footer_rows,
                    'overlay_width': popup_max_col,
                    'overlay_height': popup_max_row
                }

            popup_widget = AutoCompletePopUp(
                self._mediator,
                self._keymapper.autocomplete_popup,
                *args, **kwargs)

            return popup_widget, get_autocomplete_popup_params
        self._autocomplete_popup_factory = autocomplete_factory

        def help_factory(*args, **kwargs):
            def get_help_popup_params(original_widget, pop_up_widget, size):
                popup_max_col, popup_max_row = pop_up_widget.pack(size)
                max_col, max_row = size
                logger.debug(f"{popup_max_col}, {popup_max_row}, {max_col},"
                             f" {max_row}")
                return {
                    'left': int((max_col - popup_max_col) / 2),
                    'top': int((max_row - popup_max_row) / 2),
                    'overlay_width': popup_max_col + 2,
                    'overlay_height': popup_max_row + 2
                }
            popup_widget = HelpPopUp(
                self._keymapper.detailed_help(),
                self._mediator,
                self._keymapper.help_popup)
            return popup_widget, get_help_popup_params
        self._help_popup_factory = help_factory

        # pyfx view frame, the UI for the whole screen
        self._view_frame = ViewFrame(
            self._screen,
            # bodies
            {"json_browser": self._json_browser},
            # footers
            {
                "help": self._help_bar,
                "query_bar": self._query_bar
            },
            {
                "autocomplete": self._autocomplete_popup_factory,
                "help": self._help_popup_factory
            },
            default_body="json_browser",
            default_footer="help",
            keymapper=self._keymapper.view_frame)
        self._mediator.register("view_frame", "size",
                                self._view_frame.size)
        self._mediator.register("view_frame", "focus",
                                self._view_frame.focus)
        self._mediator.register("view_frame", "open_pop_up",
                                self._view_frame.open_pop_up)
        self._mediator.register("view_frame", "close_pop_up",
                                self._view_frame.close_pop_up)

        # Pyfx view manager, manages UI life cycle
        self._view = View(self._view_frame, self._screen, self._config.view)

    def add_node_creator(self, node_creator):
        """Customizes rendering behavior in Pyfx of any Python types.

        Args:
            `node_creator`(JSONNodeCreatory): An instance of
                :class:`~.view.json_lib.json_node_creator.JSONNodeCreator`.
                It creates a specific type of :class:`.JSONSimpleNode` based on
                the type of the value.

            .. note::
               `node_creator` will take precedence than any predefined node
               creators in Pyfx, thus ``None`` is a valid input for it.
        """
        self._node_factory.register(node_creator)

    def run(self):
        """Starts Pyfx."""
        try:
            self.__init()
            self.__run()
        except PyfxException as e:
            # Identified exception, will gonna print to stderr
            raise e
        except Exception as e:
            # We gonna swallow unknown error here
            # so that pyfx exit quietly
            logger.opt(exception=True).\
                error("Unknown exception encountered in app.run, "
                      "exit with {}", e)
        finally:
            self._thread_pool_executor.shutdown(wait=True)
            self._screen.clear()

    def __init(self):
        """Post-initializes Pyfx, it must be called before `__run()`.

        .. note::
           `__init__()`: Used to construct all Pyfx dependencies and load all
           the static configuration files.

           `__init()`: Used to initialize all the dependencies, such as
           processing data to construct essential widgets.
        """
        logger.debug("Initializing Pyfx...")
        self._json_browser.refresh_view(self._data)

    def __run(self):
        """Starts the UI loop."""
        logger.debug("Running Pyfx...")
        self._view.run()

    def __init_logger(self, is_debug_mode):
        logger.configure(
            handlers=[{
                "sink": "/tmp/pyfx.log",
                "level": "DEBUG" if is_debug_mode else "INFO",
                "enqueue": True,
                "rotation": "5MB",
                "retention": "10 days",
                "format": "<green>{time}</green> {module}.{function} "
                          "<level>{message}</level>"
            }])

    def __read_config(self, config_path):
        logger.debug("Loading Pyfx configuration...")
        return parse(config_path)

    def __create_screen(self):
        """Creates a `urwid.raw_display.Screen` and turn off control."""
        # Specify the `input` to force Screen reload the value for sys.stdin
        # as sys.stdin may be redirected. E.g., when pyfx is using with pipe,
        # we replaced the sys.stdin at the CLI level
        screen = urwid.raw_display.Screen(input=sys.stdin)
        # noinspection PyBroadException
        try:
            # this is to turn off control for SIGTERM while in pyfx
            screen.tty_signal_keys('undefined', 'undefined', 'undefined',
                                   'undefined', 'undefined')
        except Exception:
            # avoid potential error during e2e test
            pass
        return screen

    def __short_help(self):
        description = [("title", "Pyfx"), "        "]
        description.extend(self._config.view.keymap.mapping.short_help())
        return description

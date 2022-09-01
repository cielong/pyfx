from enum import Enum

import urwid
from loguru import logger
from overrides import overrides

from .common import PopUpLauncher
from .keymapper import KeyDefinition


class FocusArea(Enum):
    """
    Enum for focus area in Main Window
    """
    BODY = "body"
    FOOTER = "footer"


class ViewFrameKeys(KeyDefinition, Enum):
    """
    Keys defined for View frame.
    """
    EXIT = "q", "Quit Pyfx."
    OPEN_HELP_PAGE = "?", "Open help page."


class ViewFrame(PopUpLauncher):
    """
    A wrapper of the frame as the main UI of `pyfx`.
    """

    def __init__(self, screen, bodies, footers, popups_factory,
                 default_body, default_footer, keymapper):
        self._screen = screen
        self._bodies = bodies
        self._footers = footers
        self._popup_factories = popups_factory
        self._keymapper = keymapper
        super().__init__(urwid.Frame(self._bodies[default_body],
                                     footer=self._footers[default_footer]))

    def focus(self, widget_name):
        if widget_name in self._bodies:
            self._change_widget_and_focus(widget_name, FocusArea.BODY)
        elif widget_name in self._footers:
            self._change_widget_and_focus(widget_name, FocusArea.FOOTER)

    def size(self, widget_name):
        """
        Get the size of the respected widget
        """
        col, row = self._screen.get_cols_rows()
        if widget_name in self._bodies:
            return col, row - 1
        elif widget_name in self._footers:
            return col, 1
        return 0, 0

    def _change_widget_and_focus(self, widget_name, area):
        if area == FocusArea.BODY:
            widget = self._bodies[widget_name]
            self.original_widget.body = widget
            self.original_widget.focus_position = FocusArea.BODY.value
        elif area == FocusArea.FOOTER:
            widget = self._footers[widget_name]
            self.original_widget.footer = widget
            self.original_widget.focus_position = FocusArea.FOOTER.value
        else:
            # swallow this error but log warnings
            logger.warning(
                "Unknown area {} for switching widgets.",
                area.value
            )

    # This is a workaround we used to be able to popup autocomplete window in
    # query bar
    # The implementation of PopUpLauncher only support pop up within the
    # launcher's canvas, i.e., autocomplete-edit's popup launcher should be
    # implemented in the container widget of the edit widget
    @overrides
    def create_pop_up(self, *args, **kwargs):
        popup_factory = kwargs['pop_up_type']
        del kwargs['pop_up_type']
        return self._popup_factories[popup_factory](*args, **kwargs)

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == ViewFrameKeys.OPEN_HELP_PAGE.key:
            self.open_pop_up("view_frame", "open_pop_up",
                             pop_up_type="help")
            return
        elif key == ViewFrameKeys.EXIT.key:
            raise urwid.ExitMainLoop()

        return key

from enum import Enum

import urwid
from loguru import logger
from overrides import overrides

from .common import PopUpLauncher


class FocusArea(Enum):
    """
    Enum for focus area in Main Window
    """
    BODY = "body"
    FOOTER = "footer"


class ViewFrame(PopUpLauncher):
    """
    A wrapper of the frame as the main UI of `pyfx`.
    """

    def __init__(self, screen, bodies, footers, popups_factory, default_body,
                 default_footer):
        self._screen = screen
        self._bodies = bodies
        self._footers = footers
        self._popup_factories = popups_factory
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
        # TODO: generalize this to allow create different popups
        return self._popup_factories["autocomplete_popup_factory"](*args,
                                                                   **kwargs)

    @overrides
    def get_pop_up_parameters(self, size, *args, **kwargs):
        cur_col, _ = self.original_widget.get_cursor_coords(size)
        popup_max_col, popup_max_row = self.pop_up_widget.pack(size)
        max_col, max_row = size
        footer_rows = self.original_widget.footer.rows((max_col,))
        return {
            'left': cur_col,
            'top': max_row - popup_max_row - footer_rows,
            'overlay_width': popup_max_col,
            'overlay_height': popup_max_row
        }

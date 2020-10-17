from enum import Enum

import urwid
from loguru import logger
from overrides import overrides

from .common import PopUpLauncher
from .components import AutoCompletePopUp


class ViewFrame(PopUpLauncher):
    """
    A wrapper of the frame as the main UI of `pyfx`.
    """

    def __init__(self, controller, body, footer):
        self._controller = controller
        super().__init__(urwid.Frame(body, footer=footer))

    def change_widget(self, widget, area):
        if area == FocusArea.BODY:
            self.original_widget.body = widget
        elif area == FocusArea.FOOTER:
            self.original_widget.footer = widget
        else:
            # swallow this error but log warnings
            logger.warning("Unknown area {} for switching widgets.", area.value)

    def change_focus(self, area):
        self.original_widget.focus_position = area.value

    @overrides
    def create_pop_up(self, widget, prefix, options):
        return AutoCompletePopUp(self, self._controller, widget, prefix, options)

    @overrides
    def get_pop_up_parameters(self, size):
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


class FocusArea(Enum):
    """
    Enum for focus area in Main Window
    """
    BODY = "body"
    FOOTER = "footer"

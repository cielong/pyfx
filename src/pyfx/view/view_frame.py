from collections import defaultdict
from enum import Enum

import urwid
from loguru import logger
from overrides import overrides

from .common import PopUpLauncher
from .components import JSONBrowser, QueryBar, HelpBar, AutoCompletePopUp


class ViewFrame(PopUpLauncher):
    """
    A wrapper of the frame as the main UI of `pyfx`.
    """

    def __init__(self, client, view_manager, keymapper):
        self._manager = view_manager
        self._keymapper = keymapper
        self._handlers = defaultdict(list)

        self._json_browser = JSONBrowser(self, keymapper.json_browser)
        self._query_bar = QueryBar(self, client, keymapper.query_bar)
        self._help_bar = HelpBar(self)

        super().__init__(urwid.Frame(self._json_browser, footer=self._help_bar))
        # json browser
        self.register("open_query_bar", self.focus_on_query)
        # autocomplete
        self.register("close_pop_up", self.close_pop_up)
        # query bar
        self.register("open_pop_up", self.open_pop_up)
        self.register("focus_on_view", self.focus_on_view)
        self.register("get_component_size", self.size)

    def notify(self, signal, source, *args, **kwargs):
        """
        Broadcast signals to all the listeners registered for the signal and
        collect result.
        """
        try:
            results = []
            for callback in self._handlers[signal]:
                results.append(callback(*args, **kwargs))
            return results
        except KeyError:
            logger.opt(exception=True) \
                .warning(f"Key ({source}, {signal}) is not defined")

    def register(self, signal, callback):
        """
        Handlers defines a set of signals this view frame will broadcast to,
        it is the callback's responsibility to filter out unused signal based on
        passed source.
        """
        self._handlers[signal].append(callback)

    def size(self):
        return self._manager.size()

    def set_data(self, data):
        self._json_browser.set_top_node(data)

    def focus_on_view(self):
        if self.original_widget.body is not self._json_browser:
            self._change_widget(self._json_browser, FocusArea.BODY)
        self._change_focus(FocusArea.BODY)

    def focus_on_query(self):
        if self.original_widget.footer is not self._query_bar:
            self._query_bar.setup()
            self._change_widget(self._query_bar, FocusArea.FOOTER)
        self._change_focus(FocusArea.FOOTER)

    def _change_widget(self, widget, area):
        if area == FocusArea.BODY:
            self.original_widget.body = widget
        elif area == FocusArea.FOOTER:
            self.original_widget.footer = widget
        else:
            # swallow this error but log warnings
            logger.warning(
                "Unknown area {} for switching widgets.",
                area.value
            )

    def _change_focus(self, area):
        self.original_widget.focus_position = area.value

    # This is a workaround we used to be able to popup autocomplete window in
    # query bar
    # The implementation of PopUpLauncher only support pop up within the
    # launcher's canvas, i.e., autocomplete-edit's popup launcher should be
    # implemented in the container widget of the edit widget
    @overrides
    def create_pop_up(self, *args, **kwargs):
        return AutoCompletePopUp(
            self, self._keymapper.autocomplete_popup, *args, **kwargs
        )

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


class FocusArea(Enum):
    """
    Enum for focus area in Main Window
    """
    BODY = "body"
    FOOTER = "footer"

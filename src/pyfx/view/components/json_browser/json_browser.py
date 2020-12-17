from enum import Enum

import urwid
from overrides import overrides

from ...json_lib import JSONListBox
from ...json_lib import JSONListWalker
from ...json_lib import NodeFactory


class JSONBrowserKeys(Enum):
    # keys for json lib
    CURSOR_UP = "up"
    CURSOR_DOWN = "down"
    TOGGLE_EXPANSION = "enter"
    # keys for switching window
    OPEN_QUERY_BAR = "."


class JSONBrowser(urwid.WidgetWrap):
    """
    Window to display JSON contents.
    """

    def __init__(self, mediator, keymapper, data=""):
        self._keymapper = keymapper
        self._mediator = mediator
        self._top_node = NodeFactory.create_node("", data, display_key=False)
        super().__init__(self._load_widget())

    def set_top_node(self, data):
        self._top_node = NodeFactory.create_node("", data, display_key=False)
        self._refresh()

    def _load_widget(self):
        listbox = JSONListBox(JSONListWalker(self._top_node))
        return urwid.AttrMap(listbox, "body")

    def _refresh(self):
        self._w = self._load_widget()

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == JSONBrowserKeys.OPEN_QUERY_BAR.value:
            self._mediator.notify("json_browser", "query")
            return

        return key

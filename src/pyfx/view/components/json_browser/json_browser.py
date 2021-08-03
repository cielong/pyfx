from enum import Enum

import urwid
from overrides import overrides

from ...json_lib import JSONListBox
from ...json_lib import JSONListWalker
from ...json_lib import NodeFactory
from ...json_lib import DEFAULT_NODE_IMPLS


class JSONBrowserKeys(Enum):
    # keys for json lib
    CURSOR_UP = "up"
    CURSOR_DOWN = "down"
    COLLAPSE_ALL = "c"
    EXPAND_ALL = "e"
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
        self._node_factory = NodeFactory(DEFAULT_NODE_IMPLS)
        self._top_node = self._node_factory.create_root_node(data)

        super().__init__(self._load_widget())
        self._mediator.register("refresh_view", self.set_top_node)

    def set_top_node(self, data):
        self._top_node = self._node_factory.create_node(
            "", data, display_key=False
        )
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
            self._mediator.notify("open_query_bar", "json_browser")
            return

        return key

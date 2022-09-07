from enum import Enum

import urwid
from overrides import overrides

from ...json_lib import JSONListBox
from ...json_lib import JSONListWalker
from ...keymapper import KeyDefinition


class JSONBrowserKeys(KeyDefinition, Enum):
    # keys for json lib
    CURSOR_UP = "up", "Move cursor up from the current line."
    CURSOR_DOWN = "down", "Move cursor down from the current line."
    COLLAPSE_ALL = "c", "Collapse all the node."
    EXPAND_ALL = "e", "Expand all the node."
    TOGGLE_EXPANSION = "enter", \
                       "Toggle to expand/collapse the current JSON node."

    # keys for switching window
    OPEN_QUERY_BAR = ".", "Open the query bar to type JSONPath."


class JSONBrowser(urwid.WidgetWrap):
    """
    Window to display JSON contents.
    """

    def __init__(self, node_factory, mediator, keymapper):
        self._node_factory = node_factory
        self._keymapper = keymapper
        self._mediator = mediator
        super().__init__(self._load_widget(None))

    def refresh_view(self, data):
        self._w = self._load_widget(data)

    @overrides
    def keypress(self, size, key):
        key = self._keymapper.key(key)
        key = super().keypress(size, key)

        if key == JSONBrowserKeys.OPEN_QUERY_BAR.key:
            self._mediator.notify("json_browser", "focus", "query_bar")
            return

        return key

    def _load_widget(self, data):
        listbox = JSONListBox(JSONListWalker(data,
                                             node_factory=self._node_factory))
        return urwid.AttrMap(listbox, "body")

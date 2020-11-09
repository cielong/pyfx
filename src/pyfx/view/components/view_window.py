import urwid
from overrides import overrides

from ..json_lib import JSONListBox
from ..json_lib import JSONListWalker
from ..json_lib import NodeFactory
from ..keymap import DefaultKeyMapping, ENTER_QUERY_WINDOW


class ViewWindow(urwid.WidgetWrap):
    """
    Window to display JSON contents.
    """

    def __init__(self, manager, data="", keymap=DefaultKeyMapping()):
        self._keymap = keymap
        self._manager = manager
        data = ViewWindow._validate(data)
        self._top_node = NodeFactory.create_node("", data, display_key=False)
        super().__init__(self._load_widget())

    def set_top_node(self, data):
        data = ViewWindow._validate(data)
        self._top_node = NodeFactory.create_node("", data, display_key=False)
        self._refresh()

    def _load_widget(self):
        listbox = JSONListBox(JSONListWalker(self._top_node), keymap=self._keymap)
        return urwid.AttrWrap(listbox, "body")

    def _refresh(self):
        self._w = self._load_widget()

    @staticmethod
    def _validate(data):
        """
        Validates input data and reset it into empty string if it is None.
        :param data: JSON valid data, could be `dict`, `list`, `int`, `str`, `float` etc.
        :return: original data, or empty string if None
        """
        return data if data else ""

    @overrides
    def keypress(self, size, key):
        key = super().keypress(size, key)
        if self._keymap.key(key) == ENTER_QUERY_WINDOW:
            self._manager.enter_query_window()
        return key

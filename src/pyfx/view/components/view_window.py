import urwid

from ..json_lib import node_factory
from ..json_lib.json_listbox import JSONListBox
from ..json_lib.json_listwalker import JSONListWalker


class ViewWindow(urwid.WidgetWrap):
    def __init__(self, data=""):
        data = data if data else ""  # reset to empty string
        self._top_node = node_factory.NodeFactory.create_node("", data, display_key=False)
        super().__init__(self.load_widget())

    def set_top_node(self, data):
        data = data if data else ""  # reset to empty string
        self._top_node = node_factory.NodeFactory.create_node("", data, display_key=False)
        self._refresh()

    def load_widget(self):
        listbox = JSONListBox(JSONListWalker(self._top_node))
        return urwid.AttrWrap(listbox, "body")

    def _refresh(self):
        self._w = self.load_widget()

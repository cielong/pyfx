import urwid

from pyfx.view.json_lib.json_listbox import JSONListBox
from pyfx.view.json_lib.json_listwalker import JSONListWalker
from pyfx.view.json_lib import node_factory


class ViewWindow(urwid.WidgetWrap):
    def __init__(self, data=""):
        data = data if data else ""  # reset to empty string
        self._top_node = node_factory.NodeFactory.create_node("", data, display_key=False)
        super().__init__(self.create_widget_from_top_node())

    def set_data(self, data):
        data = data if data else ""  # reset to empty string
        self._top_node = node_factory.NodeFactory.create_node("", data, display_key=False)
        self._w._invalidate()
        self._set_w(self.create_widget_from_top_node())

    def create_widget_from_top_node(self):
        listbox = JSONListBox(JSONListWalker(self._top_node))
        return urwid.AttrWrap(listbox, "body")

import urwid

from ..json_lib import node_factory
from ..json_lib.json_listbox import JSONListBox
from ..json_lib.json_listwalker import JSONListWalker


class ViewWindow(urwid.WidgetWrap):
    """
    Window to display JSON contents.
    """

    def __init__(self, data=""):
        data = ViewWindow._validate(data)
        self._top_node = node_factory.NodeFactory.create_node("", data, display_key=False)
        super().__init__(self.load_widget())

    def set_top_node(self, data):
        data = ViewWindow._validate(data)
        self._top_node = node_factory.NodeFactory.create_node("", data, display_key=False)
        self._refresh()

    def load_widget(self):
        listbox = JSONListBox(JSONListWalker(self._top_node))
        return urwid.AttrWrap(listbox, "body")

    def _refresh(self):
        self._w = self.load_widget()

    @staticmethod
    def _validate(data):
        """
        Validates input data and reset it into empty string if it is None.
        :param data: JSON valid data, could be `dict`, `list`, `int`, `str`, `float` etc.
        :return: original data, or empty string if None
        """
        return data if data else ""

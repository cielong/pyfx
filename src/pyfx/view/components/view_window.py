import urwid

from ..json_lib import JSONListBox, JSONListWalker, NodeFactory


class ViewWindow(urwid.WidgetWrap):
    """
    Window to display JSON contents.
    """

    def __init__(self, data=""):
        data = ViewWindow._validate(data)
        self._top_node = NodeFactory.create_node("", data, display_key=False)
        super().__init__(self._load_widget())

    def set_top_node(self, data):
        data = ViewWindow._validate(data)
        self._top_node = NodeFactory.create_node("", data, display_key=False)
        self._refresh()

    def _load_widget(self):
        listbox = JSONListBox(JSONListWalker(self._top_node))
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

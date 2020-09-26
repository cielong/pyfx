import urwid

from pyfx.view.json_listbox import JSONListBox
from pyfx.view.json_listwalker import JSONListWalker
from pyfx.view.models.node_factory import NodeFactory


class View:
    """ UI entry point for pyfx """

    palette = [
        ('body', 'black', 'light gray'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('head', 'yellow', 'black', 'standout'),
        ('foot', 'light gray', 'black'),
        ('key', 'light cyan', 'black', 'underline'),
        ('title', 'white', 'black', 'bold'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
    ]

    footer_text = [
        ('title', "Pyfx"), "    ",
        ('key', "UP"), ",", ('key', "DOWN"), ",",
        ('key', "PAGE UP"), ",", ('key', "PAGE DOWN"), "  ",
        ('key', "+"), ",",
        ('key', "-"), "  ",
        ('key', "LEFT"), "  ",
        ('key', "HOME"), "  ",
        ('key', "END"), "  ",
        ('key', "Q"),
    ]

    def __init__(self, controller):
        self._controller = controller
        self._data = None
        self._header = urwid.AttrWrap(urwid.Text(""), "head")
        self._footer = urwid.AttrWrap(urwid.Text(self.footer_text), "foot")

    def set_data(self, data):
        self._data = data

    def main_window(self):
        top_node = NodeFactory.create_node("", self._data, display_key=False)
        listbox = JSONListBox(JSONListWalker(top_node))
        listbox.offset_rows = 1
        return urwid.Frame(
            urwid.AttrWrap(listbox, "body"),
            header=self._header,
            footer=self._footer
        )

    @staticmethod
    def unhandled_input(k):
        if k in ('q', 'Q'):
            raise urwid.ExitMainLoop(Exception("Exit."))

#! /usr/bin/env python3

import json
import urwid
from pyfx.ui.json_listbox import JSONListBox
from pyfx.ui.json_listwalker import JSONListWalker
from pyfx.ui.models.atomic_node import AtomicNode
from pyfx.ui.models.array_node import ArrayNode
from pyfx.ui.models.object_node import ObjectNode

from typing import NoReturn


class Browser:
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

    def __init__(self, file=None):
        data = Browser.validate_and_load(file)
        self.top_node = Browser.set_top_node(data)
        self.listbox = JSONListBox(JSONListWalker(self.top_node))
        self.listbox.offset_rows = 1
        self.header = urwid.Text("")
        self.footer = urwid.Text(self.footer_text)
        self.view = urwid.Frame(
            urwid.AttrWrap(self.listbox, 'body'),
            header=urwid.AttrWrap(self.header, 'head'),
            footer=urwid.AttrWrap(self.footer, 'foot')
        )
        self.loop = urwid.MainLoop(self.view, self.palette,
                                   unhandled_input=Browser.unhandled_input)

    def main(self) -> NoReturn:
        self.loop.run()

    @staticmethod
    def set_top_node(data) -> "JSONNode":
        if isinstance(data, list):
            return ArrayNode("", data, display_key=False)
        elif isinstance(data, dict):
            return ObjectNode("", data, display_key=False)
        else:
            return AtomicNode("", data, display_key=False)

    @staticmethod
    def unhandled_input(k):
        if k in ('q', 'Q'):
            raise urwid.ExitMainLoop(Exception("Exit."))

    @staticmethod
    def validate_and_load(file: str):
        if file is None:
            raise urwid.ExitMainLoop(Exception("JSON file is None, exit."))
        try:
            with open(file, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise urwid.ExitMainLoop(e)

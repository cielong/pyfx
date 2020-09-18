#! /usr/bin/env python3

import json
import urwid
from .models.ObjectNode import ObjectNode


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
        self.top_node = ObjectNode(data)
        self.listbox = urwid.TreeListBox(urwid.TreeWalker(self.top_node))
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

    def main(self) -> None:
        self.loop.run()

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

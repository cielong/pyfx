#! /usr/bin/env python3

import urwid
from ..widgets.AtomicWidget import AtomicWidget


class AtomicNode(urwid.TreeNode):
    """Display widget for string, integer, number, boolean and null"""
    def load_widget(self):
        return AtomicWidget(self)

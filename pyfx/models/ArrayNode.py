#! /usr/bin/env python3

import urwid
from ..widgets.ArrayWidget import ArrayWidget


class ArrayNode(urwid.TreeNode):
    """List Type Json Node"""
    def load_widget(self):
        return ArrayWidget(self)

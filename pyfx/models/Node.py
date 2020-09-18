#! /usr/bin/env python3

import urwid
from ..widgets.NodeWidget import NodeWidget


class Node(urwid.TreeNode):
    """Display widget for leaf nodes"""
    def load_widget(self):
        return NodeWidget(self)

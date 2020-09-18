#! /usr/bin/env python3

import urwid
from .Node import Node
from ..widgets.ParentNodeWidget import ParentNodeWidget


class ParentNode(urwid.ParentNode):
    """Display widget for non-leaf nodes"""
    def load_widget(self):
        return ParentNodeWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        if isinstance(data, dict):
            return list(data.keys())
        else:
            return range(len(data))

    def load_child_node(self, key):
        child_data = self.get_value()[key]
        child_depth = self.get_depth() + 1
        if isinstance(child_data, list) or isinstance(child_data, dict):
            child_class = ParentNode
        else:
            child_class = Node
        return child_class(child_data, parent=self, key=key, depth=child_depth)

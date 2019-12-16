#! /usr/bin/env python3

import urwid
from .Node import Node
from ..widgets.ParentNodeWidget import ParentNodeWidget

class ParentNode(urwid.ParentNode):
    """Display widget for object type nodes"""
    def load_widget(self):
        return ParentNodeWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        if isinstance(data, dict):
            return list(data.keys())
        else:
            return range(len(data))

    def load_child_node(self, key):
        childdata = self.get_value()[key]
        childdepth = self.get_depth() + 1
        if isinstance(childdata, list) or isinstance(childdata, dict):
            childclass = ParentNode
        else:
            childclass = Node
        return childclass(childdata, parent=self, key=key, depth=childdepth)

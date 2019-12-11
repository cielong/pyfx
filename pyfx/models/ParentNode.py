#! /usr/bin/env python3

import urwid
from .Node import Node
from ..widgets.NodeWidget import NodeWidget

class ParentNode(urwid.ParentNode):
    """Display widget for interior/parent nodes"""
    def load_widget(self):
        return NodeWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        return range(len(data['children']))

    def load_child_node(self, key):
        childdata = self.get_value()['children'][key]
        childdepth = self.get_depth() + 1
        if 'children' in childdata:
            childclass = ParentNode
        else:
            childclass = Node
        return childclass(childdata, parent=self, key=key, depth=childdepth)

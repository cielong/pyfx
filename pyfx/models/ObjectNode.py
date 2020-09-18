#! /usr/bin/env python3

import urwid
from .AtomicNode import AtomicNode
from .ArrayNode import ArrayNode
from ..widgets.ObjectWidget import ObjectWidget


class ObjectNode(urwid.ParentNode):
    """Display widget for non-leaf nodes"""
    def load_widget(self):
        return ObjectWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        if isinstance(data, dict):
            return list(data.keys())
        else:
            return range(len(data))

    def load_child_node(self, key):
        child_data = self.get_value()[key]
        child_depth = self.get_depth() + 1
        if isinstance(child_data, dict):
            child_class = ObjectNode
        elif isinstance(child_data, list):
            child_class = ArrayNode
        else:
            child_class = AtomicNode
        return child_class(child_data, parent=self, key=key, depth=child_depth)

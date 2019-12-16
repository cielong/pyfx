#! /usr/bin/env python3

import urwid

class ListNode(urwid.TreeNode):
    """List Type Json Node"""
    def load_widget(self):
        return NodeWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        return range(len(data))

    def load_child_node(self, key):
        childdata = self.get_value()

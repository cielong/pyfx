#! /usr/bin/env python3

import urwid


class NodeWidget(urwid.TreeWidget):
    """Display widget for leaf nodes"""
    def get_display_text(self):
        key = self.get_node().get_key()
        value = self.get_node().get_value()
        return f"{key}: {value}"

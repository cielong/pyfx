#! /usr/bin/env python3

import urwid

class NodeWidget(urwid.TreeWidget):
    """Display widget for leaf nodes"""
    def get_display_text(self):
        return self.get_node().get_value()['name']
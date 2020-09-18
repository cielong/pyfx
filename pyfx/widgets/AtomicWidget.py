#! /usr/bin/env python3

import urwid


class AtomicWidget(urwid.TreeWidget):
    """Display widget for leaf nodes"""
    def get_display_text(self):
        key = self.get_node().get_key()
        value = self.get_node().get_value()
        if value is None:
            return f"{key}: null"
        else:
            return f"{key}: {value}"

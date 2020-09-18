#! /usr/bin/env python3

import urwid


class ArrayWidget(urwid.TreeWidget):
    """Display widget for list"""
    def get_display_text(self):
        key = self.get_node().get_key()
        value = ", ".join([str(v) for v in self.get_node().get_value()])
        return f"{key}: [{value}]"

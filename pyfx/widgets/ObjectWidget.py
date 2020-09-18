#! /usr/bin/env python3

import urwid


class ObjectWidget(urwid.TreeWidget):
    """Display widget for object nodes"""
    def get_display_text(self):
        if self.get_node().get_depth() == 0:
            return ""
        else:
            return self.get_node().get_key()

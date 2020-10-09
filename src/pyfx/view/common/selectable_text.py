import urwid
from overrides import overrides


class SelectableText(urwid.Text):
    @overrides
    def selectable(self):
        return True

    def keypress(self, size, key):
        """ don't handle key """
        return key
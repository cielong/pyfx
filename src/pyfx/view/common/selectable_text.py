import urwid
from overrides import overrides


class SelectableText(urwid.Text):
    """A text widgets can be focused on.

    The widget is used in any :py:class:`urwid.ListBox` to make each text
    section being selectable, i.e. being focused on.
    """

    @overrides
    def selectable(self) -> bool:
        return True

    def keypress(self, size, key):
        """ :py:func:`keypress` is required for any selectable widgets. """
        # don't handle any key
        return key

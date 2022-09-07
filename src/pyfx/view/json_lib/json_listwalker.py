import urwid
from overrides import overrides

from .json_node_factory import JSONNodeFactory


class JSONListWalker(urwid.ListWalker):
    """

    """

    def __init__(self, content,
                 node_factory=JSONNodeFactory()):
        self._focus = node_factory.create_root_node(content)

    # focus
    @overrides
    def get_focus(self):
        if self._focus is None:
            return None, None
        widget = self._focus.get_widget()
        return widget, self._focus

    def set_focus(self, focus):
        self._focus = focus
        self._modified()

    @overrides
    def get_next(self, position):
        widget = position.get_widget()
        target = widget.next_inorder()
        if target is None:
            return None, None

        return target, target.get_node()

    @overrides
    def get_prev(self, position):
        widget = position.get_widget()
        target = widget.prev_inorder()
        if target is None:
            return None, None

        return target, target.get_node()

from abc import ABCMeta
from abc import abstractmethod


class JSONCompositeEndNode(metaclass=ABCMeta):
    """
    base implementation for a end node attached to each composite node
    which represents the end of a composite node.

    this node is used to distinguish between start node, so when visiting
    each node in a tree, the widget for that position could be uniquely
    identified. this is required by JSONListWalker.

    all of the methods other than loading widget will be delegate to the
    attaching composite node.
    """

    def __init__(self, start_node):
        self._start_node = start_node
        # ui
        self._widget = None

    def is_end_node(self):
        return True

    def is_expanded(self):
        return self._start_node.is_expanded()

    def collapse_all(self):
        return self._start_node.collapse_all()

    def toggle_expanded(self):
        self._start_node.toggle_expanded()

    def get_start_node(self):
        return self._start_node

    def get_depth(self):
        return self._start_node.get_depth()

    def get_parent(self):
        return self._start_node.get_parent()

    def get_last_child(self):
        return self._start_node.get_last_child()

    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #
    def get_widget(self):
        if self._widget is None:
            self._widget = self.load_widget()
        return self._widget

    @abstractmethod
    def load_widget(self):
        raise NotImplementedError(
            f"{type(self)} does not implement abstract method #load_widget"
        )

    # =================================================================================== #
    # sibling methods                                                                     #
    # =================================================================================== #
    def next_sibling(self):
        return self._start_node.next_sibling()

    def prev_sibling(self):
        return self._start_node.prev_sibling()

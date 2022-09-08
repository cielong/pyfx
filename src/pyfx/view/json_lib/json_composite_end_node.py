"""Ending representation of a non-leaf node in the tree."""

from abc import ABCMeta
from abc import abstractmethod


class JSONCompositeEndNode(metaclass=ABCMeta):
    """Base implementation to represent an ending of a composite node.

    This is mostly used to better distinguish between a start widget and a end
    widget in a composite node, while iterating the tree in
    :class:`.JSONListWalker`.

    For example, with an object JSON structure:

    .. code-block:: python
       :linenos:

       {
         "key": "value"
       }

    When user clicks '}' by mouse, in order to know the current focus position
    is at the end of a composite node, we need to store this information
    somewhere different from the node represents '{'.
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

    def get_widget(self):
        if self._widget is None:
            self._widget = self.load_widget()
        return self._widget

    @abstractmethod
    def load_widget(self):
        raise NotImplementedError(
            f"{type(self)} does not implement abstract method #load_widget"
        )

    def next_sibling(self):
        return self._start_node.next_sibling()

    def prev_sibling(self):
        return self._start_node.prev_sibling()

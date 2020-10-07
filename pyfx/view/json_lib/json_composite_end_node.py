from abc import ABCMeta
from abc import abstractmethod


class JSONCompositeEndNode(metaclass=ABCMeta):
    """ a special node which represents the end of a composite node. """

    def __init__(self,
                 start_node
                 ):
        self._start_node = start_node
        # ui
        self._widget = None

    def is_end_node(self):
        return True

    def is_expanded(self):
        return self._start_node.is_expanded()

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
        raise AttributeError(f"{type(self)} does not implement abstract method #load_widget")

    # =================================================================================== #
    # sibling methods                                                                     #
    # =================================================================================== #
    def next_sibling(self):
        return self._start_node.next_sibling()

    def prev_sibling(self):
        return self._start_node.prev_sibling()

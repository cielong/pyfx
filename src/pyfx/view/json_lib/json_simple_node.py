from abc import ABCMeta
from abc import abstractmethod

import urwid


class JSONSimpleNode(metaclass=ABCMeta):
    """
    base leaf node to store JSON contents and cache JSONWidget.
    a JSONNode consists of the following elements:
    *  key: accessor token for parent nodes
    *  value: subclass-specific data
    *  parent: a JSONNode which contains a pointer back to this object (only ObjectNode, ArrayNode)
    *  depth: the depth of the current node
    *  root: the root of the whole tree
    *  widget: the widget used to render the object
    """

    def __init__(self, key, value, parent=None, display_key=True):
        self._index_assigner = None
        self._index = None

        # current node key
        self._key = key
        self._value = value

        # relationship to other nodes
        self._parent = parent
        self._depth = None
        self._root = None

        # view
        self._display_key = display_key
        self._widget = None

    def __str__(self):
        """
        NodeType{key, value}
        """
        return f"{type(self).__name__}{{key:{self._key}, value:{self._value}}}"

    def __repr__(self):
        """
        NodeType{key, value}
        """
        return f"{type(self).__name__}{{key:{self._key}, value:{self._value}}}"

    def is_end_node(self):
        return False

    # =================================================================================== #
    # getters and setters                                                                 #
    # =================================================================================== #

    # index
    def get_index(self):
        return self._index

    def set_index(self, index):
        self._index = index

    def get_max_row_index(self):
        if self._index_assigner is None:
            return -1
        return self._index_assigner.max_row_index

    def assign_index(self, assigner):
        self._index_assigner = assigner
        self._index_assigner.visit(self)

    # key
    def get_key(self):
        return self._key

    # value
    def get_value(self):
        return self._value

    # parent
    def get_parent(self):
        if self._parent is None and self.get_depth() > 0:
            raise urwid.ExitMainLoop(Exception("Parent is None while depth is non-zero"))
        return self._parent

    # depth
    def get_depth(self):
        if self._depth is None:
            self._depth = self.__calculate_depth()
        return self._depth

    def __calculate_depth(self):
        """ recursively calculate the current depth """
        if self._parent is None:
            return 0
        return self._parent.get_depth() + 1

    # root
    def get_root(self):
        """ lazy getter for root """
        if self._root is None:
            self._root = self.__load_root()
        return self._root

    def __load_root(self):
        root = self
        while root._parent is not None:
            root = root._parent
        return root

    def is_root(self) -> bool:
        return self._parent is None

    # display_key
    def is_display_key(self):
        return self._display_key

    def is_expanded(self):
        return True

    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    # widget
    def get_widget(self):
        """ cache and return the widget for the current node """
        if self._widget is None:
            self._widget = self.load_widget()
        return self._widget

    @abstractmethod
    def load_widget(self):
        raise NotImplementedError(
            f"{type(self)} does not implement #load_widget."
        )

    # =================================================================================== #
    # sibling methods                                                                     #
    # =================================================================================== #

    # next sibling
    def next_sibling(self):
        if self.is_root():
            return None
        return self._parent.next_child(self._key)

    # prev sibling
    def prev_sibling(self):
        if self.is_root():
            return None
        return self._parent.prev_child(self._key)

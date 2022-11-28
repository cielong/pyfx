"""Contains the data model for a leaf JSON tree node.

.. rubric:: Background

Pyfx models a JSON as a tree and the leaf of the tree represents the values
inside the JSON data. For example,

.. code-block::
   :linenos:

   [
      {
        "Name": "John",
        "Age": 18
      }
   ]

Both values (**John** and **18**) are leaf nodes, while all the other
parenthesis are non-leaf nodes.

Both leaf and non-leaf nodes are a data model to store the actual JSON data
and its relative position information inside the tree (such as *parent*, *depth*
etc), so that the constructed tree support tree walking and random accessing.
E.g., see :class:`.primitive.string.StringNode`.

.. rubric:: Urwid Widget

Additionally, the node also creates and caches its related UI rendering unit
during runtime for better starting time. For details about the UI rendering unit
see :class:`.JSONWidget` for details.
E.g., see :class:`.primitive.string.StringWidget`
"""
from abc import ABCMeta
from abc import abstractmethod

import urwid


class JSONSimpleNode(metaclass=ABCMeta):
    """Leaf node to store JSON contents and cache JSONWidget.

    Attributes:
        _key (Any): accessor token for parent nodes.
        _value (Any): subclass-specific data.
        _parent(JSONCompositeNode): a node which contains a pointer back to this
            object.
        _depth(int): the depth of the current node.
        _root(JSONSimpleNode): the root of the whole tree.
        _widget(JSONWidget): the widget used to render the object.
    """

    def __init__(self, key, value, parent=None, display_key=True):
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

    def is_end_node(self):
        return False

    # ====================================================================== #
    # getters and setters                                                    #
    # ====================================================================== #

    # key
    def get_key(self):
        return self._key

    # value
    def get_value(self):
        return self._value

    # parent
    def get_parent(self):
        if self._parent is None and self.get_depth() > 0:
            raise urwid.ExitMainLoop(
                Exception("Parent is None while depth is non-zero")
            )
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
        return self.get_depth() == 0

    # display_key
    def is_display_key(self):
        return self._display_key

    def is_expanded(self):
        return True

    # ===================================================================== #
    # ui                                                                    #
    # ===================================================================== #

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

    # ====================================================================== #
    # sibling methods                                                        #
    # ====================================================================== #

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

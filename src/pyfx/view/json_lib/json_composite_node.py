"""Contains the data model for a **non-leaf** JSON tree node.

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

Different from :class:`.JSONSimpleNode`, a non-leaf node does not represents any
real JSON data, instead it can be seen as a virtual node that is created for
tree traversing and to represent the UI edges (e.g. '{' and '}').

There are two separate components to represent a non-leaf node, namely
:class:`.JSONCompositeNode` and :class:`.JSONCompositeEndNode`.

* :class:`.JSONCompositeNode`:
    Conceptually, this is the real non-leaf nodes.
    There are two UI units stored inside this class, an unexpanded widget and a
    starting widget. While rendering, depending on the current state (whether
    the node is expanded or not), Pyfx will choose the correct widgets.
    E.g., see :class:`.object.object_node.ObjectNode`.

* :class:`.JSONCompositeEndNode`:
    Conceptually, this is a meta node attached to :class:`.JSONCompositeNode`.
    This class is created with the single purpose of representing the ending
    edges of the non-leaf nodes and it delegates all the necessary methods to
    the attached :class:`.JSONCompositeNode`.
    This is required for tree traversing with random node accessing, so that we
    can determine the type of the current focused widget, and thus the correct
    position for picking the right siblings.
    E.g., see :class:`.object.object_end_node.ObjectEndNode`.

.. rubric:: Urwid Widget

Similar to :class:`.JSONSimpleNode`, both components of a non-leaf node creates
and caches the UI unit during runtime.

However, to be able to support node expansion and collapsing, there are in total
3 kind widgets cached inside a composite node, representing the unexpanded,
starting and ending edges. All of the widgets shares the same structure as
:class:`.JSONWidget`.
E.g., see :class:`.object.object_end_widget.ObjectEndWidget`.
"""

from abc import ABCMeta
from abc import abstractmethod

from overrides import final
from overrides import overrides

from .json_simple_node import JSONSimpleNode


class JSONCompositeNode(JSONSimpleNode, metaclass=ABCMeta):
    """
    base node represents a JSON `object` or `array` type, also a non-leaf node
    in the whole parsed tree.
    """

    def __init__(self, key, value, node_factory, parent=None, display_key=True
                 ):
        super().__init__(key, value, parent, display_key)
        self._node_factory = node_factory
        # only display the first layer on start
        self._expanded = self.is_root()
        self._start_widget = None
        self._unexpanded_widget = None
        self._end_node = None

    # expanded
    def is_expanded(self):
        return self._expanded

    def toggle_expanded(self):
        self._expanded = not self._expanded

    @abstractmethod
    def collapse_all(self):
        pass

    @abstractmethod
    def has_children(self):
        pass

    @abstractmethod
    def get_first_child(self):
        pass

    @abstractmethod
    def get_last_child(self):
        pass

    @abstractmethod
    def prev_child(self, key):
        pass

    @abstractmethod
    def next_child(self, key):
        pass

    # end_node
    def get_end_node(self):
        if not self.is_expanded():
            # unexpanded node is itself the end node
            return self
        if self._end_node is None:
            self._end_node = self.load_end_node()
        return self._end_node

    @abstractmethod
    def load_end_node(self):
        pass

    @final
    @overrides
    def get_widget(self):
        if not self.is_expanded():
            return self.get_unexpanded_widget()
        return self.get_start_widget()

    @final
    @overrides
    def load_widget(self):
        raise NotImplementedError(f"{type(self)} is a composite node and does "
                                  "not have #load_widget() method.")

    # start widget
    def get_start_widget(self):
        if self._start_widget is None:
            self._start_widget = self.load_start_widget()
        return self._start_widget

    @abstractmethod
    def load_start_widget(self):
        pass

    # unexpanded widget
    def get_unexpanded_widget(self):
        if self._unexpanded_widget is None:
            self._unexpanded_widget = self.load_unexpanded_widget()
        return self._unexpanded_widget

    @abstractmethod
    def load_unexpanded_widget(self):
        pass

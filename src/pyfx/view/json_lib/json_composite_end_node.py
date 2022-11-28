"""Ending representation of a **non-leaf** node in the tree.

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

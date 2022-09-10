"""Data and UI models used for JSON rendering.

.. rubric:: Description

Pyfx models JSON as a tree of :class:`.JSONSimpleNode` and creates a urwid
widget (:class:`.JSONListBox`) to help rendering the tree on the screen.

.. rubric:: Public Interfaces

Inside this json_lib module, there are four exposed classes in this module,
namely :class:`.JSONListBox`, :class:`.JSONListWalker`,
:class:`.JSONNodeFactory` and :class:`.JSONNodeCreator`.

* :class:`.JSONListBox`:
   A component handles keypress and mouse events.
   It converts those signals into actual action on the UI widgets.
* :class:`.JSONListWalker`:
   A separate component handles JSON tree traversal.
   It determines the prev and next UI widget inside :class:`.JSONListBox`.
* :class:`.JSONNodeFactory`:
    The facade class which composes different :class:`.JSONNodeCreator` to
    perform type deduction on the value and create the node in the tree.
* :class:`.JSONNodeCreator`:
    The public factory interface to create a specific :class:`.JSONSimpleNode`
    instance if matches the actual type.

.. rubric:: Data Modeling

The JSON data is loaded into memory as a tree.
The leaf node of the tree represents the values inside the JSON data (
represented by :class:`.JSONSimpleNode`), while the non-leaf node of the tree
represents a logical group of values such as `object` or `array`. For example,

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

.. rubric:: Examples

1. Create a :class:`.JSONListBox` widget that can be used in urwid TUI.

.. code-block:: python
   :linenos:

   from pyfx.json_lib import JSONListBox
   from pyfx.json_lib import JSONListWalker

   # create JSONListBox from data
   listbox = JSONListBox(JSONListWalker(data))

2. Uses a customize rendering widgets for an user-defined class.

.. code-block:: python
   :linenos:

   from pyfx.json_lib import JSONListBox
   from pyfx.json_lib import JSONListWalker
   from pyfx.json_lib.json_node_factory import JSONNodeFactory
   from pyfx.json_lib.json_node_creator import JSONNodeCreator

   class UserNodeCreator(JSONNodeCreator):
       def create_node(self, key, value, **kwargs):
           return StringNode(key, str(value), **kwargs)

   # create a customize JSONNodeFactory
   node_factory = JSONNodeFactory()
   node_factory.register(UserNodeCreator())

   # create JSONListBox from data using the customize node_factory
   listbox = JSONListBox(JSONListWalker(data, node_factory=node_factory))
"""
from .json_listbox import JSONListBox
from .json_listwalker import JSONListWalker

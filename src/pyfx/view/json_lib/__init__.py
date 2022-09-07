"""Data and UI models used for JSON rendering.

.. rubric:: Description

Pyfx models JSON rendering as :class:`.JSONListBox` a subclass of
:class:`urwid.ListBox`, similar to :class:`urwid.TreeListBox`.

There are two exposed classes in this module, namely :class:`.JSONListBox`,
:class:`.JSONListWalker`:

* :class:`.JSONListBox`:
   A component handles keypress and mouse events.
   It converts those signals into actual action on the UI widgets.
* :class:`.JSONListWalker`:
   A separate component handles actual JSON tree iteration.
   It determines the prev and next UI widget inside :class:`.JSONListBox`.

.. rubric:: Data Modeling

The JSON data is loaded into memory as a tree and each node in the tree is an
instance of subclass of :class:`.JSONSimpleNode` for leaf nodes or
:class:`.JSONCompositeNode` for non-leaf nodes.

Regarding node creation, :class:`.JSONNodeFactory` and :class:`.JSONNodeCreator`
are the key classes:

* :class:`.JSONNodeFactory`:
    The facade class which composes different :class:`.JSONNodeCreator` to try
    and create a node.
* :class:`.JSONNodeCreator`:
    The factory class to create a specific :class:`.JSONSimpleNode` instance.

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

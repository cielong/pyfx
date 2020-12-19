"""
A collection of JSON rendering related data models and widgets.

Example
=======
.. code-block:: python
   :linenos:

    from pyfx.view.json_lib import JSONListBox, JSONListWalker, NodeFactory

    # 1. create top node from the data (only supports dict, list and primitive variable)
    top_node = NodeFactory.create_node("", data, display_key=False)

    # 2. create JSONListBox from top node, a :class:`urwid.ListBox` compatible widget
    listbox = JSONListBox(JSONListWalker(top_node))

    # 3. use listbox in your own TUI

Implementation Details
======================

Exposed Class
-------------

For integrated this class into your own TUI, three classes is the most and the only entry point.

* :class:`.JSONListBox`
    A :class:`urwid.ListBox` compatible class to manage the visible portion and rendering of the
    JSON tree.
* :class:`.JSONListWalker`
    A :class:`urwid.ListWalker` compatible class to manage the traverse of the whole tree and
    store the current focus node.
* :class:`.NodeFactory`
    A factory to create node based on its value type.

Data Modeling
-------------

The JSON data is loaded into memory as a tree and based on the data type it creates

- Non-leaf Nodes (`array`, `object`)

  Each non-leaf node, two types of nodes are implemented to ease navigation and rendering:

  - Start node / Unexpanded node to represent start / unexpanded line
  - End node to represent end line.

- Leaf Nodes (`string`, `integer`, `numeric`, `boolean`, `null`)

  Each leaf node, single node is enough for navigation.
"""
from .json_listbox import JSONListBox
from .json_listwalker import JSONListWalker
from .node_factory import NodeFactory

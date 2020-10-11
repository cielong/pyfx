"""
A collection of JSON rendering related data models and widgets, implemented using urwid.

Usage
=====
For integrated this class into your own TUI, three classes is the most and the only entry point.

* :py:class:`.json_listbox.JSONListBox`
    A :py:class:`urwid.ListBox` compatible class to manage the visible portion and rendering of the
    JSON tree.
* :py:class:`.json_listwalker.JSONListWalker`
    A :py:class:`urwid.ListWalker` compatible class to manage the traverse of the whole tree and
    store the current focus node.
* :py:class:`.node_factory.NodeFactory`
    A factory to create node based on its value type.

Example
-------
.. code-block:: python

    from pyfx.view.json_lib import JSONListBox, JSONListWalker, NodeFactory

    # create top node from the data (only supports dict, list and primitive variable)
    top_node = NodeFactory.create_node("", data, display_key=False)
    # create JSONListBox from top node, a :py:class:`urwid.ListBox` compatible widget
    listbox = JSONListBox(JSONListWalker(top_node))
    # use listbox in your own TUI
    ...

Data Modeling
=============

The JSON data is loaded into memory as a tree and different JSON type are cluster into
non-leaf nodes (`array`, `object`) and leaf nodes (`string`, `integer`, `numeric`,
`boolean`, `null`).

For each non-leaf node, it implements
:py:class:`.json_composite_node.JSONCompositeNode` for start line and
:py:class:`.json_composite_end_node.JSONCompositeEndNode` for end line.

For each leaf node, it implements :py:class:`.json_simple_node.JSONSimpleNode`.
"""
from .json_listbox import JSONListBox
from .json_listbox import JSONListWalker
from .node_factory import NodeFactory

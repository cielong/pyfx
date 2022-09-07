"""A collection of data models and widgets used for JSON rendering.

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

Example
=======
.. code-block:: python
   :linenos:

   from pyfx.json_lib import JSONListBox
   from pyfx.json_lib import JSONListWalker

   # ...
   # create JSONListBox from data
   listbox = JSONListBox(JSONListWalker(data))


Data Modeling
=============
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
"""
from .json_listbox import JSONListBox
from .json_listwalker import JSONListWalker

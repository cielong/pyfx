"""A collection of data models and widgets used for JSON rendering.

Pyfx models JSON rendering as :class:`.JSONListBox` a subclass of
:class:`urwid.ListBox`, similar to :class:`urwid.TreeListBox`.

There are three exposed class in that this module, namely :class:`.JSONListBox`,
:class:`.JSONListWalker`:

* :class:`.JSONListBox`:
   A component handles keypress and mouse events.
   It converts those signals into actual action on the UI widgets.
* :class:`.JSONListWalker`:
   A separate component handles actual JSON tree iteration.
   It determines the prev and next UI widget inside :class:`.JSONListBox`.

The JSON data is loaded into memory as a tree and based on the data type it
creates.

- Non-leaf Nodes (`array`, `object`)

  Each non-leaf node, two types of nodes are implemented to ease navigation and rendering:

  - Start node / Unexpanded node to represent start / unexpanded line
  - End node to represent end line.

- Leaf Nodes (`string`, `integer`, `numeric`, `boolean`, `null`)

  Each leaf node, single node is enough for navigation.
"""
from .json_listbox import JSONListBox
from .json_listwalker import JSONListWalker

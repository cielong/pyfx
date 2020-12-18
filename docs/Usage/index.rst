=====
Usage
=====

You can use *pyfx* in two ways:
* A standalone CLI tool
* A python module which can be integrated in any python CLI application

CLI
======================

.. click:: pyfx.cli:main
   :prog: pyfx

Python Module
=============

Directly Attach *pyfx* Simple TUI
=================================
Directly integrate *pyfx*'s TUI into your own project.
Normally, one would expect this to be the last step of your CLI application. The method `Controller#run_with_data` contains a infinite loop [MainLoop](http://urwid.org/reference/main_loop.html#mainloop) to render image until exit.

.. code-block:: python
   :linenos:
   :emphasize-lines: 1,5

    from pyfx import Controller

    # data is the what you want to render as TUI
    # only supports dict, list and primitive variable
    Controller().run_with_data(data)

Integrate with Your Own urwid-based TUI
=======================================
You can also import *pyfx* native JSON lib to integrate it into your own urwid TUI, e.g. [json_browser.py](src/pyfx/view/components/json_browser/json_browser.py).

.. code-block:: python
   :linenos:
   :emphasize-lines: 1,4,6

    from pyfx.view.json_lib import JSONListBox, JSONListWalker, NodeFactory

    # 1. create top node from the data (only supports dict, list and primitive variable)
    top_node = NodeFactory.create_node("", data, display_key=False)
    # 2. create JSONListBox from top node
    listbox = JSONListBox(JSONListWalker(top_node))
    # 3. use listbox in your own TUI

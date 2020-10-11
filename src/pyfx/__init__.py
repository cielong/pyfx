"""
A python-native command line JSON viewer with fully JSONPath support.

Usage
=====
Aside from the included CLI command, `pyfx` can be easily integrated into any python
CLI application. There are two types integration,

* Direct plug-in `pyfx`'s native TUI, which rendering the JSON output of your program to
  the user.

* Import :py:mod:`pyfx.view.json_lib` to integrate `pyfx`'s JSON widgets into your own
  TUI.

Direct Plug-in TUI
------------------
:py:class:`.core.Controller` is main entry point, when one only needs to direct plug in
the TUI to render the output to its user.

.. code-block:: python

    from pyfx import Controller

    # data is the what you want to render as TUI
    # only supports dict, list and primitive variable
    Controller().run_with_data(data)
    ...

`Notice` one would expect, this is the last step of your TUI to show the user your program's
JSON output.

Use JSON widgets
----------------
For details please refer :py:mod:`pyfx.view.json_lib`.
"""
from .core import Controller

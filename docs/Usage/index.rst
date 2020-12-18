=====
Usage
=====

You can use *pyfx* in two ways:

- A standalone CLI tool

- A python module which can be integrated in any python CLI application

.. contents:: Table of Content
   :local:
   :depth: 2
   :backlinks: none

CLI
======================

.. click:: pyfx.cli:main
   :prog: pyfx

Python Module
=============

Directly Attach *Pyfx* Simple TUI
---------------------------------
Directly integrate *Pyfx*'s TUI into your own project, see
`example <../Reference/controller.html#example>`__ for details.

Integrate with Your Own Urwid-based TUI
---------------------------------------
Integrate *Pyfx* native JSON-lib into your own Urwid-based TUI, see
`example <../References/view.html#example>`__ for details.

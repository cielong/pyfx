===================
Theme Configuration
===================

Theme configures the color scheme of *Pyfx* used, when presenting the JSON data.

.. contents:: Table of Content
   :local:
   :depth: 2
   :backlinks: none

Schema
======

Theme is configured with the following configuration schema under `view configuration <view.html>`_.

.. code-block:: yaml
   :linenos:

   view:
     appearance:
       theme: string, accepted_options = ["basic"]

Each :code:`theme` is mapped to a separate color-scheme configuration. For supported color,
please refer to `Urwid Display Attributes <http://urwid.org/manual/displayattributes.html>`_

Basic Theme (Default)
=====================
:code:`basic` is transformed to the following color scheme.

Example
-------

+------------------+--------------------------------------------------------+------------+
| Name             | Description                                            | Color      |
+==================+========================================================+============+
| body             | Pyfx body (JSON Browser)                               |            |
+------------------+--------------------------------------------------------+------------+
| foot             | Pyfx footer (Query Bar and Help Bar)                   |            |
+------------------+--------------------------------------------------------+------------+
| focused          | Focused display                                        |            |
+------------------+--------------------------------------------------------+------------+
| **Auto Complete PopUp**                                                                |
+------------------+--------------------------------------------------------+------------+
| popup            | Autocomplete popup                                     |            |
+------------------+--------------------------------------------------------+------------+
| popup_focused    | Focused display for autocomplete popup                 |            |
+------------------+--------------------------------------------------------+------------+
| **JSON Browser**                                                                       |
+------------------+--------------------------------------------------------+------------+
| json_key         | Object key                                             |            |
+------------------+--------------------------------------------------------+------------+
| json_string      | :code:`string` type value                              |            |
+------------------+--------------------------------------------------------+------------+
| json_integer     | :code:`integer` type value                             |            |
+------------------+--------------------------------------------------------+------------+
| json_numeric     | :code:`numeric` type value                             |            |
+------------------+--------------------------------------------------------+------------+
| json_bool        | :code:`boolean` type value                             |            |
+------------------+--------------------------------------------------------+------------+
| json_null        | :code:`null` type value                                |            |
+------------------+--------------------------------------------------------+------------+
| json_focused     | Focused display for JSON                               |            |
+------------------+--------------------------------------------------------+------------+

Color Scheme Configuration
--------------------------
.. code-block:: yaml
   :linenos:

    # default setting for Pyfx body (JSON Browser)
    body:
      foreground: "default"  # Terminal default
      background: "default"  # Terminal default

    # default setting for Pyfx footer (Query Bar | Help Bar)
    foot:
      foreground: "light gray"
      background: "default"

    # default setting for focused display
    focused:
      foreground: "light gray"
      background: "dark blue"

    # autocomplete popup
    popup:
      foreground: "black"
      background: "light cyan"

    # focused color for autocomplete popup
    popup_focused:
      foreground: "white"
      background: "dark magenta"

    # json browser
    json_key:
      foreground: "light blue"
      background: "default"

    json_string:
      foreground: "light green"
      background: "default"

    json_integer:
      foreground: "light cyan"
      background: "default"

    json_numeric:
      foreground: "light cyan"
      background: "default"

    json_bool:
      foreground: "yellow"
      background: "default"

    json_null:
      foreground: "light red"
      background: "default"

    json_focused:
      foreground: "light gray"
      background: "dark blue"
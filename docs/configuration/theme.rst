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

Color Scheme Table
------------------

+------------------+--------------------------------------------------------+--------------------+
| Name             | Description                                            | Foreground Color   |
+==================+========================================================+====================+
| body             | Pyfx body (JSON Browser)                               | terminal default   |
+------------------+--------------------------------------------------------+--------------------+
| foot             | Pyfx footer (Query Bar and Help Bar)                   | :gray:`000000000`  |
+------------------+--------------------------------------------------------+--------------------+
| focused          | Focused display                                        | :gray:`000000000`  |
+------------------+--------------------------------------------------------+--------------------+
| **Auto Complete PopUp**                                                                        |
+------------------+--------------------------------------------------------+--------------------+
| popup            | Autocomplete popup                                     | :black:`000000000` |
+------------------+--------------------------------------------------------+--------------------+
| popup_focused    | Focused display for autocomplete popup                 | :white:`000000000` |
+------------------+--------------------------------------------------------+--------------------+
| **JSON Browser**                                                                               |
+------------------+--------------------------------------------------------+--------------------+
| json_key         | Object key                                             | :blue:`000000000`  |
+------------------+--------------------------------------------------------+--------------------+
| json_string      | :code:`string` type value                              | :green:`000000000` |
+------------------+--------------------------------------------------------+--------------------+
| json_integer     | :code:`integer` type value                             | :cyan:`000000000`  |
+------------------+--------------------------------------------------------+--------------------+
| json_numeric     | :code:`numeric` type value                             | :cyan:`000000000`  |
+------------------+--------------------------------------------------------+--------------------+
| json_bool        | :code:`boolean` type value                             | :yellow:`000000000`|
+------------------+--------------------------------------------------------+--------------------+
| json_null        | :code:`null` type value                                | :red:`000000000`   |
+------------------+--------------------------------------------------------+--------------------+
| json_focused     | Focused display for JSON                               | :gray:`000000000`  |
+------------------+--------------------------------------------------------+--------------------+

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

=========================
Key Mapping Configuration
=========================

Key mapping configures the key and its action used in *Pyfx*.

.. contents:: Table of Content
   :local:
   :depth: 2
   :backlinks: none

Schema
======

Key mapping is configured with the following configuration schema under `view configuration <view.html>`_.

.. code-block:: yaml
   :linenos:

   view:
     keymap:
       mode: string, accepted_options = ["basic" | "emacs" | "vim"]

Basic Mode (Default)
====================

To enable, add the following configuration in your config file:

.. code-block:: yaml
   :linenos:

   keymap:
     mode: "basic"

Mapped Keys
-----------

+------------------+---------------------------------------------------+
| Key              | Function                                          |
+==================+===================================================+
| q                | exit pyfx (except in Query Bar)                   |
+------------------+---------------------------------------------------+
| **JSON Browser**                                                     |
+------------------+---------------------------------------------------+
| up               | move cursor up one line                           |
+------------------+---------------------------------------------------+
| down             | move cursor down one line                         |
+------------------+---------------------------------------------------+
| e                | expand all                                        |
+------------------+---------------------------------------------------+
| c                | collapse all                                      |
+------------------+---------------------------------------------------+
| enter            | toggle expansion                                  |
+------------------+---------------------------------------------------+
| .                | enter query window (used to input JSONPath query) |
+------------------+---------------------------------------------------+
| **Query Bar**                                                        |
+------------------+---------------------------------------------------+
| enter            | apply JSONPath query and switch to JSON Browser   |
+------------------+---------------------------------------------------+
| esc              | cancel query and restore to state before query    |
+------------------+---------------------------------------------------+

Emacs Mode
==========
To enable, add the following configuration in your config file:

.. code-block:: yaml
   :linenos:

   keymap:
     mode: "emacs"

Mapped Keys
-----------

+------------------+---------------------------------------------------+
| Key              | Function                                          |
+==================+===================================================+
| q                | exit pyfx (except in Query Bar)                   |
+------------------+---------------------------------------------------+
| **JSON Browser**                                                     |
+------------------+---------------------------------------------------+
| up / ctrl p      | move cursor up one line                           |
+------------------+---------------------------------------------------+
| down / ctrl n    | move cursor down one line                         |
+------------------+---------------------------------------------------+
| e / ctrl e       | expand all                                        |
+------------------+---------------------------------------------------+
| c / ctrl x       | collapse all                                      |
+------------------+---------------------------------------------------+
| enter            | toggle expansion                                  |
+------------------+---------------------------------------------------+
| . / meta x       | enter query window (used to input JSONPath query) |
+------------------+---------------------------------------------------+
| **Query Bar**                                                        |
+------------------+---------------------------------------------------+
| enter            | apply JSONPath query and switch to JSON Browser   |
+------------------+---------------------------------------------------+
| ctrl g           | cancel query and restore to state before query    |
+------------------+---------------------------------------------------+

Vim Mode
========
To enable, add the following configuration in your config file:

.. code-block:: yaml
   :linenos:

   keymap:
      mode: "vim"

Mapped Keys
-----------

+------------------+---------------------------------------------------+
| Key              | Function                                          |
+==================+===================================================+
| q                | exit pyfx (except in Query Bar)                   |
+------------------+---------------------------------------------------+
| **JSON Browser**                                                     |
+------------------+---------------------------------------------------+
| up / k           | move cursor up one line                           |
+------------------+---------------------------------------------------+
| down / j         | move cursor down one line                         |
+------------------+---------------------------------------------------+
| e                | expand all                                        |
+------------------+---------------------------------------------------+
| c                | collapse all                                      |
+------------------+---------------------------------------------------+
| enter            | toggle expansion                                  |
+------------------+---------------------------------------------------+
| . / :            | enter query window (used to input JSONPath query) |
+------------------+---------------------------------------------------+
| **Query Bar**                                                        |
+------------------+---------------------------------------------------+
| enter            | apply JSONPath query and switch to JSON Browser   |
+------------------+---------------------------------------------------+
| esc              | cancel query and restore to state before query    |
+------------------+---------------------------------------------------+
=============
Configuration
=============

*Pyfx* is configured using YAML. There are two ways to provide a configuration file:

- Pass directly through CLI option (:code:`-c` | :code:`--config`).

- Create a config file in predefined folders and *Pyfx* will load it with best effort and
  use the default `config <https://github.com/cielong/pyfx/blob/main/src/pyfx/config/config.yml>`_ if no one is find.

  The predefined folders are searched in following order, with the first exist one has high priority.
  1. :code:`~/.config/pyfx/config.yml`

Table of Content
================

.. toctree::
   :maxdepth: 2
   :numbered:

   view
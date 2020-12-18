=============
Configuration
=============

*Pyfx* is configured using YAML, the config file is either passed directly through CLI option ( :code:`-c / --config` ) or automatically
loaded in predefined config folder.

If no :code:`-c / --config` option, it will try to search config file with the following order:
1. ~/.config/pyfx/config.yml

As the last effort, it will resolve the package default
`config <https://github.com/cielong/pyfx/blob/master/src/pyfx/config/config.yml>`_. Please also refer to
this config as an example when creating your own config file.

.. toctree::
   :maxdepth: 2

   view
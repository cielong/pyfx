"""A collection of predefined configurations in Pyfx.

This package contains:

1. The default Pyfx configuration.
2. The predefined enum mappings for theme and key mapping.
   The public configuration file defines some enums, like those in `themes` and
   `keymaps` folders. These enums hide the detailed object used in Pyfx.
"""
import pathlib

# Exports the paths of some configuration files
yaml_path = pathlib.Path(__file__).parent

keymaps_path = yaml_path / "keymaps"
themes_path = yaml_path / "themes"

"""Components that converts a keyboard input into the defined keyboard input.

Urwid only supports condition branch to handle keyboard input, as a result, all
the components and json_libs used by Pyfx have a set of predefined hard-coded
keyboard input, see
:class:`~pyfx.view.components.json_browser.json_browser.JSONBrowserKeys`.

This module is created to allow the keyboard input configurable.

The base keymapper :class:`.AbstractComponentKeyMapper` should be called before
the keyboard handling logic to convert the actual keyboard input into a fake
keyboard signal.
"""
from .abstract_component_keymapper import AbstractComponentKeyMapper
from .abstract_component_keymapper import KeyDefinition
from .keymapper_config import KeyMapperConfiguration

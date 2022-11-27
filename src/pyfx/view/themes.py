"""Components that defines color scheme for different components inside Pyfx."""

from dataclasses import asdict
from dataclasses import dataclass

import urwid


@dataclass(frozen=True)
class ComponentTheme:
    foreground: str = urwid.DEFAULT
    background: str = urwid.DEFAULT


@dataclass(frozen=True)
class Theme:
    body: ComponentTheme = ComponentTheme()
    foot: ComponentTheme = ComponentTheme(urwid.LIGHT_GRAY)
    focused: ComponentTheme = ComponentTheme(urwid.LIGHT_GRAY, urwid.DARK_BLUE)

    # auto-complete popup
    autocomplete: ComponentTheme = ComponentTheme(urwid.BLACK, urwid.LIGHT_CYAN)
    autocomplete_focused: ComponentTheme = ComponentTheme(urwid.WHITE,
                                                          urwid.DARK_MAGENTA)

    # help popup
    help: ComponentTheme = ComponentTheme(urwid.BLACK, urwid.LIGHT_GRAY)
    help_focused: ComponentTheme = ComponentTheme(urwid.WHITE, urwid.DARK_GRAY)

    # json
    json_key: ComponentTheme = ComponentTheme(urwid.LIGHT_BLUE)
    json_string: ComponentTheme = ComponentTheme(urwid.LIGHT_GREEN)
    json_integer: ComponentTheme = ComponentTheme(urwid.LIGHT_CYAN)
    json_numeric: ComponentTheme = ComponentTheme(urwid.LIGHT_CYAN)
    json_bool: ComponentTheme = ComponentTheme(urwid.YELLOW)
    json_null: ComponentTheme = ComponentTheme(urwid.LIGHT_RED)
    json_focused: ComponentTheme = ComponentTheme(urwid.LIGHT_GRAY,
                                                  urwid.DARK_BLUE)

    def palette(self):
        palette = []
        for component_name, component_theme in asdict(self).items():
            component_name = component_name.replace('_', '.')
            palette.append([
                component_name,
                component_theme["foreground"],
                component_theme["background"]
            ])
        return palette

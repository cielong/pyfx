from dataclasses import dataclass, asdict

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

    # auto-complete
    popup: ComponentTheme = ComponentTheme(urwid.BLACK, urwid.LIGHT_CYAN)
    popup_focused: ComponentTheme = ComponentTheme(
        urwid.WHITE, urwid.DARK_MAGENTA
    )

    # json
    json_key: ComponentTheme = ComponentTheme(urwid.LIGHT_BLUE)
    json_string: ComponentTheme = ComponentTheme(urwid.LIGHT_GREEN)
    json_integer: ComponentTheme = ComponentTheme(urwid.LIGHT_CYAN)
    json_numeric: ComponentTheme = ComponentTheme(urwid.LIGHT_CYAN)
    json_bool: ComponentTheme = ComponentTheme(urwid.YELLOW)
    json_null: ComponentTheme = ComponentTheme(urwid.LIGHT_RED)
    json_focused: ComponentTheme = ComponentTheme(
        urwid.LIGHT_GRAY, urwid.DARK_BLUE
    )

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

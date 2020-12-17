from dataclasses import dataclass, field

from .theme_config_parser import create_palette
from .theme import Theme


@dataclass(frozen=True)
class ThemeConfiguration:
    theme: str = "basic"

    color_scheme: Theme = field(init=False)

    def __post_init__(self):
        # replace theme name with actual palette scheme
        object.__setattr__(self, "color_scheme", create_palette(self.theme))

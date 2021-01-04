from dataclasses import dataclass

from pyfx.view.keymapper.keymapper_config import KeyMapperConfiguration
from pyfx.view.theme.theme_config import ThemeConfiguration


@dataclass(frozen=True)
class ViewConfiguration:
    row_number: bool = True
    appearance: ThemeConfiguration = ThemeConfiguration()
    keymap: KeyMapperConfiguration = KeyMapperConfiguration()

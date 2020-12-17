from dataclasses import dataclass

from pyfx.view.keymapper import KeyMapperConfiguration
from pyfx.view.theme import ThemeConfiguration


@dataclass(frozen=True)
class ViewConfiguration:
    appearance: ThemeConfiguration = ThemeConfiguration()
    keymap: KeyMapperConfiguration = KeyMapperConfiguration()

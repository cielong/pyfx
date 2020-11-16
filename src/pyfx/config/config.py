from dataclasses import dataclass

from ..view.keymapper import KeyMapperConfiguration


@dataclass
class Configuration:
    keymap: KeyMapperConfiguration = KeyMapperConfiguration()

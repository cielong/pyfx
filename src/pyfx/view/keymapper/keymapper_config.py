from dataclasses import dataclass, field

from .keymapper_config_parser import create_keymapper
from .keymapper import KeyMapper


@dataclass(frozen=True)
class KeyMapperConfiguration:
    mode: str = 'basic'

    mapping: KeyMapper = field(init=False)

    def __post_init__(self):
        # replace `mode` with actual key mapping
        object.__setattr__(self, 'mapping', create_keymapper(self.mode))

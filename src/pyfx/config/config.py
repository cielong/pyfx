from dataclasses import dataclass


@dataclass(frozen=True)
class KeyMapConfiguration:
    """Configuration for keys."""
    mode: str = 'basic'


@dataclass(frozen=True)
class UIConfiguration:
    """Configurations for UI"""
    theme: str = "basic"
    keymap: KeyMapConfiguration = KeyMapConfiguration()


@dataclass
class PyfxConfiguration:
    ui: UIConfiguration = UIConfiguration()

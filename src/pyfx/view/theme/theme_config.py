from dataclasses import dataclass


@dataclass(frozen=True)
class ThemeConfiguration:
    theme: str = "basic"

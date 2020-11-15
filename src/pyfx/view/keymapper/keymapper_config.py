from dataclasses import dataclass


@dataclass(frozen=True)
class KeyMapperConfiguration:
    mode: str = "basic"

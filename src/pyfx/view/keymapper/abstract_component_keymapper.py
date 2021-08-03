from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class AbstractComponentKeyMapper(ABC):
    """
    Base Key Mapping
    """

    @property
    @abstractmethod
    def mapped_key(self):
        raise NotImplementedError(
            f"mapped_key is not implemented in {type(self)}"
        )

    def key(self, key):
        if key in self.mapped_key:
            return self.mapped_key[key].value
        return key

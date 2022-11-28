from abc import ABC, abstractmethod
from dataclasses import dataclass
from collections import namedtuple


KeyDefinition = namedtuple('KeyDefinition', ["key", "description"])


@dataclass(frozen=True)
class BaseComponentKeyMapper(ABC):
    """
    Base Key Mapping
    """

    @property
    @abstractmethod
    def mapped_key(self):
        """All the mapped keys for a component."""
        raise NotImplementedError(
            f"mapped_key is not implemented in {type(self)}"
        )

    @property
    @abstractmethod
    def short_help(self):
        """A brief description for all the keys inside the current component."""
        raise NotImplementedError(
            f"short_help is not implemented in {type(self)}")

    @property
    @abstractmethod
    def detailed_help(self):
        """A detailed description for all the keys inside the current component.
        """
        raise NotImplementedError(
            f"detailed_help is not implemented in {type(self)}")

    def key(self, key):
        """Remaps the key into the original key definition, so that they can be
        recognized.
        """
        if key in self.mapped_key:
            return self.mapped_key[key].key
        return key

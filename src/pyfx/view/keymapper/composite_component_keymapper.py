from dataclasses import dataclass, field

from overrides import overrides

from .abstract_component_keymapper import AbstractComponentKeyMapper


@dataclass(frozen=True)
class CompositeKeyMapper(AbstractComponentKeyMapper):
    """
    Composite multiple key mappings and return the action if any of the key mapping
    contains the mapping key.
    """
    keymappers: field(default_factory=list)

    # noinspection PyMissingConstructor
    def __init__(self, keymappers):
        CompositeKeyMapper._validate_keymappers(keymappers)
        self.__setattr__("keymappers", keymappers)

    @property
    def mapped_key(self):
        return {}

    @overrides
    def key(self, key):
        for keymapper in self.keymappers:
            action = keymapper.key(key)
            if action is not None:
                return action
        return key

    @staticmethod
    def _validate_keymappers(keymappers):
        """
        Validates key mappers to avoid ambiguous key mappings defined in key mappers
        """
        keymapper_types = set([type(keymapper) for keymapper in keymappers])
        if len(keymapper_types) > 1:
            raise ValueError("keymappers belongs to different components.")

        mapped_keys = {}
        for keymapper in keymappers:
            for key in keymapper.mapped_keys:
                if key in mapped_keys and mapped_keys[key] != keymapper.mapped_keys[key]:
                    raise ValueError(f"""keymappers contains ambiguous key {key} defined:
                                         [{mapped_keys[key].name}, {keymapper.mapped_keys[key].name}]""")
                mapped_keys[key] = keymapper.mapped_keys[key]

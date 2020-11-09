from overrides import overrides

from .abstract_keymap import AbstractKeyMapping


class CompositeKeyMapping(AbstractKeyMapping):
    """
    Composite multiple key mappings and return the action if any of the key mapping
    contains the mapping key.
    """

    # noinspection PyMissingConstructor
    def __init__(self, key_mappings):
        self._key_mappings = key_mappings

    @overrides
    def key(self, key):
        for key_mapping in self._key_mappings:
            action = key_mapping.key(key)
            if action is not None:
                return action
        return None

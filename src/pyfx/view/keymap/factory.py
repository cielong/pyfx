from . import DefaultKeyMapping, EmacsKeyMapping, VimKeyMapping, CompositeKeyMapping


class KeyMapFactory:
    _keymap = {
        "default": DefaultKeyMapping,
        "emacs": EmacsKeyMapping,
        "vi": VimKeyMapping
    }

    @staticmethod
    def keymap(modes):
        if len(modes) == 1:
            return KeyMapFactory._keymap[modes[0]]()

        key_mappings = [KeyMapFactory._keymap[m]() for m in modes]
        return CompositeKeyMapping(key_mappings)

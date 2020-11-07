from abc import ABC

from .constants import CURSOR_UP, CURSOR_DOWN, ACTIVATE, ENTER_QUERY_WINDOW, EXIT_QUERY_WINDOW


class AbstractKeyMapping(ABC):

    _key_mapping = {}
    _actions = {
        "_cursor_up": CURSOR_UP,
        "_cursor_down": CURSOR_DOWN,
        "_activate": ACTIVATE,
        "_enter_query_window": ENTER_QUERY_WINDOW,
        "_exit_query_window": EXIT_QUERY_WINDOW
    }

    def __init__(self, cursor_up, cursor_down, activate, enter_query_window, exit_query_window):
        self._cursor_up = cursor_up
        self._cursor_down = cursor_down
        self._activate = activate
        self._enter_query_window = enter_query_window
        self._exit_query_window = exit_query_window

        self.__configure_keys()

    def key(self, key):
        if key not in self._key_mapping:
            return None
        return self._key_mapping[key]

    def __configure_keys(self):
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                if value in self._key_mapping and self._key_mapping[value] != self._actions[key]:
                    raise KeyMappingException(f"Ambiguous key `{value}` maps to multiple action.")
                self._key_mapping[value] = self._actions[key]
            elif isinstance(value, list):
                for k in value:
                    if k in self._key_mapping and self._key_mapping[k] != self._actions[key]:
                        raise KeyMappingException(f"Ambiguous key `{value}` maps to multiple action.")
                    self._key_mapping[k] = self._actions[key]


class KeyMappingException(Exception):
    pass

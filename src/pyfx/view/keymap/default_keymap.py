from .abstract_keymap import AbstractKeyMapping


class DefaultKeyMapping(AbstractKeyMapping):
    """
    KeyMapping support normal direction keys.
    """

    def __init__(self):
        super().__init__(
            cursor_up="up",
            cursor_down="down",
            activate="enter",
            enter_query_window=".",
            exit_query_window="esc"
        )

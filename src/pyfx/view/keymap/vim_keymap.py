from .abstract_keymap import AbstractKeyMapping


class VimKeyMapping(AbstractKeyMapping):
    def __init__(self):
        super().__init__(
            cursor_up="k",
            cursor_down="j",
            activate="enter",
            enter_query_window=":",
            exit_query_window="esc"
        )

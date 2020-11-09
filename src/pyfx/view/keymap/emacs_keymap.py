from ..keymap.abstract_keymap import AbstractKeyMapping


class EmacsKeyMapping(AbstractKeyMapping):
    """
    Emacs-like key mapping.
    """

    def __init__(self):
        super().__init__(
            cursor_up="ctrl p",
            cursor_down="ctrl n",
            activate="enter",
            enter_query_window="meta x",
            exit_query_window="ctrl g"
        )

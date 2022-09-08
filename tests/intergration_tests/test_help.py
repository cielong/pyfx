import unittest

from parameterized import parameterized_class

from pyfx import PyfxApp
from pyfx.config import parse
from tests.fixtures import FIXTURES_DIR
from tests.fixtures.keys import split


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class HelpIT(unittest.TestCase):
    """
    Integration tests for query and auto-completion working flow.
    """

    def setUp(self):
        self.config_path = FIXTURES_DIR / self.config_file

    def test_help_exit(self):
        """
        Test navigate and select one auto-complete options.
        """
        data = {
            "alice": "0",
            "bob": "1",
            "chuck": "2",
            "daniel": "3"
        }

        app = PyfxApp(data=data, config=self.config_path)
        view = app._view
        keymap = app._keymapper

        inputs = split([
            # 1. enter query bar
            keymap.view_frame.open_help_page,
            # 2. move down in the help popup
            keymap.help_popup.cursor_down,
            # 3. move down in the help popup
            keymap.help_popup.cursor_down,
            # 4. move up in the help popup
            keymap.help_popup.cursor_up,
            # 5. exit help
            keymap.help_popup.exit,
            # 6. exit pyfx
            keymap.view_frame.exit
        ], keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertEqual(True, result, err)

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
        self.config = parse(FIXTURES_DIR / self.config_file)
        self.keymap = self.config.view.keymap.mapping

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

        app = PyfxApp(data=data, config=self.config)
        view = app._view

        inputs = split([
            # 1. enter query bar
            self.keymap.view_frame.open_help_page,
            # 2. move down in the help popup
            self.keymap.help_popup.cursor_down,
            # 3. move down in the help popup
            self.keymap.help_popup.cursor_down,
            # 4. move up in the help popup
            self.keymap.help_popup.cursor_up,
            # 5. exit help
            self.keymap.help_popup.exit,
            # 6. exit pyfx
            self.keymap.exit
        ], self.keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertEqual(True, result, err)

import unittest

from parameterized import parameterized_class

from pyfx import PyfxApp
from tests.fixtures import FIXTURES_DIR
from tests.fixtures.keys import split


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class SavingIT(unittest.TestCase):
    """Integration tests for saving working flow."""

    def setUp(self):
        self.config_path = FIXTURES_DIR / self.config_file

    def test_save_query_results_and_cancel(self):
        """Test invoking saving workflow and then cancel."""

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
            # invoke saving
            keymap.json_browser.open_save_bar,
            "t",
            keymap.save_bar.cancel,
            keymap.json_browser.exit
        ], keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertTrue(result, err)
        self.assertEqual(app._query_bar, app._view_frame.mini_buffer)

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
class WarningIT(unittest.TestCase):
    """
    Integration tests for warning working flow.
    """

    def setUp(self):
        self.config_path = FIXTURES_DIR / self.config_file

    def test_warning_bar_in_json_browser(self):
        """
        Test warning update and show up.
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
            # enter an undefined key in json browser
            'ctrl q'
        ], keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertFalse(result, err)
        self.assertEqual(app._warning_bar,
                         app._view_frame.original_widget.mini_buffer)
        self.assertEqual(app._warning_bar.message(),
                         "Unknown key `ctrl q`. Press `?` for all supported "
                         "keys.")

        inputs = split([
            # enter valid key in json browser
            keymap.json_browser.open_help_page,
            # close help pop up
            keymap.help_popup.exit,
            # exit Pyfx
            keymap.json_browser.exit
        ], keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertTrue(result, err)
        self.assertEqual(app._query_bar,
                         app._view_frame.original_widget.mini_buffer)

    def test_warning_bar_in_query_bar(self):
        """
        Test warning update and show up.
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
            # enter query bar
            keymap.json_browser.open_query_bar,
            # enter an undefined key in json browser
            'ctrl q'
        ], keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertFalse(result, err)
        self.assertEqual(app._warning_bar,
                         app._view_frame.original_widget.mini_buffer)
        self.assertEqual(app._warning_bar.message(),
                         "Unknown key `ctrl q`. Press any keys to continue.")

        inputs = split([
            # exit query bar
            keymap.query_bar.cancel,
            # exit Pyfx
            keymap.json_browser.exit
        ], keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertTrue(result, err)
        self.assertEqual(app._query_bar,
                         app._view_frame.original_widget.mini_buffer)

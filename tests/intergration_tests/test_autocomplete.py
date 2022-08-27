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
class AutoCompleteIT(unittest.TestCase):
    """
    Integration tests for query and auto-completion working flow.
    """

    def setUp(self):
        self.config = parse(FIXTURES_DIR / self.config_file)
        self.keymap = self.config.view.keymap.mapping

    def test_autocomplete_select(self):
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
            self.keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. move down in the autocomplete popup
            self.keymap.autocomplete_popup.cursor_down,
            # 4. select option
            self.keymap.autocomplete_popup.select,
            # 5. apply query and switch to json browser
            self.keymap.query_bar.query,
            # 6. exit
            self.keymap.exit
        ], self.keymap.global_command_key)

        result, err = view.process_input(inputs)
        self.assertEqual(True, result, err)

    def test_autocomplete_cancel(self):
        """
        Test navigate and cancel auto-complete.
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
            self.keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. move down in the autocomplete popup twice
            self.keymap.autocomplete_popup.cursor_down,
            self.keymap.autocomplete_popup.cursor_down,
            # 4. move up in the autocomplete popup
            self.keymap.autocomplete_popup.cursor_up,
            # 5. cancel autocomplete
            self.keymap.autocomplete_popup.cancel,
            # 6. remove last '.'
            "backspace",
            # 7. apply query and switch to json browser
            self.keymap.query_bar.query,
            # 8. exit
            self.keymap.exit
        ], self.keymap.global_command_key)
        result, err = view.process_input(inputs)

        self.assertEqual(True, result, err)

    def test_autocomplete_navigation(self):
        """
        Test navigation in auto-complete, particularly with pressing
        navigation key at the start or end of the list.
        """
        data = {
            "alice": "0",
            "bob": "1"
        }

        app = PyfxApp(data=data, config=self.config)
        view = app._view

        inputs = split([
            # 1. enter query bar
            self.keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. move down in the autocomplete popup third times,
            #    extra navigation key should not have any effect
            self.keymap.autocomplete_popup.cursor_down,
            self.keymap.autocomplete_popup.cursor_down,
            self.keymap.autocomplete_popup.cursor_down,
            # 4. move up in the autocomplete popup,
            #    extra navigation key should not have any effect
            self.keymap.autocomplete_popup.cursor_up,
            self.keymap.autocomplete_popup.cursor_up,
            self.keymap.autocomplete_popup.cursor_up,
            self.keymap.autocomplete_popup.cursor_up,
            # 5. select option
            self.keymap.autocomplete_popup.select,
            # 6. apply query and switch to json browser
            self.keymap.query_bar.query,
            # 7. exit
            self.keymap.exit
        ], self.keymap.global_command_key)
        result, err = view.process_input(inputs)

        self.assertEqual(True, result, err)

    def test_autocomplete_pass_keypress(self):
        """
        Test autocomplete popup pass keypress to query bar and update itself.
        """
        data = {
            "alice": "0",
            "bob": "1"
        }

        app = PyfxApp(data=data, config=self.config)
        view = app._view

        inputs = split([
            # 1. enter query bar
            self.keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. input 'a'
            "a",
            # 4. select autocomplete
            self.keymap.autocomplete_popup.select,
            # 5. apply query and switch to json browser
            self.keymap.query_bar.query,
            # 6. exit
            self.keymap.exit
        ], self.keymap.global_command_key)
        result, err = view.process_input(inputs)

        self.assertEqual(True, result, err)

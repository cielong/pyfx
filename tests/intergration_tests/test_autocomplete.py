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
class AutoCompleteIT(unittest.TestCase):
    """
    Integration tests for query and auto-completion working flow.
    """

    def setUp(self):
        self.config_path = FIXTURES_DIR / self.config_file

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

        app = PyfxApp(data=data, config=self.config_path)
        keymap = app._keymapper

        inputs = split([
            # 1. enter query bar
            keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. move down in the autocomplete popup
            keymap.autocomplete_popup.cursor_down,
            # 4. select option
            keymap.autocomplete_popup.select,
            # 5. apply query and switch to json browser
            keymap.query_bar.query,
            # 6. exit
            keymap.json_browser.exit
        ], keymap.global_command_key)

        result, err = app.process_input(inputs)
        self.assertTrue(result, err)

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

        app = PyfxApp(data=data, config=self.config_path)
        keymap = app._keymapper

        inputs = split([
            # 1. enter query bar
            keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. move down in the autocomplete popup twice
            keymap.autocomplete_popup.cursor_down,
            keymap.autocomplete_popup.cursor_down,
            # 4. move up in the autocomplete popup
            keymap.autocomplete_popup.cursor_up,
            # 5. cancel autocomplete
            keymap.autocomplete_popup.cancel,
            # 6. remove last '.'
            "backspace",
            # 7. apply query and switch to json browser
            keymap.query_bar.query,
            # 8. exit
            keymap.json_browser.exit
        ], keymap.global_command_key)
        result, err = app.process_input(inputs)

        self.assertTrue(result, err)

    def test_autocomplete_navigation(self):
        """
        Test navigation in auto-complete, particularly with pressing
        navigation key at the start or end of the list.
        """
        data = {
            "alice": "0",
            "bob": "1"
        }

        app = PyfxApp(data=data, config=self.config_path)
        keymap = app._keymapper

        inputs = split([
            # 1. enter query bar
            keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. move down in the autocomplete popup third times,
            #    extra navigation key should not have any effect
            keymap.autocomplete_popup.cursor_down,
            keymap.autocomplete_popup.cursor_down,
            keymap.autocomplete_popup.cursor_down,
            # 4. move up in the autocomplete popup,
            #    extra navigation key should not have any effect
            keymap.autocomplete_popup.cursor_up,
            keymap.autocomplete_popup.cursor_up,
            keymap.autocomplete_popup.cursor_up,
            keymap.autocomplete_popup.cursor_up,
            # 5. select option
            keymap.autocomplete_popup.select,
            # 6. apply query and switch to json browser
            keymap.query_bar.query,
            # 7. exit
            keymap.json_browser.exit
        ], keymap.global_command_key)
        result, err = app.process_input(inputs)

        self.assertTrue(result, err)

    def test_autocomplete_pass_keypress(self):
        """
        Test autocomplete popup pass keypress to query bar and update itself.
        """
        data = {
            "alice": "0",
            "bob": "1"
        }

        app = PyfxApp(data=data, config=self.config_path)
        keymap = app._keymapper

        inputs = split([
            # 1. enter query bar
            keymap.json_browser.open_query_bar,
            # 2. input '.'
            ".",
            # 3. input 'a'
            "a",
            # 4. select autocomplete
            keymap.autocomplete_popup.select,
            # 5. apply query and switch to json browser
            keymap.query_bar.query,
            # 6. exit
            keymap.json_browser.exit
        ], keymap.global_command_key)
        result, err = app.process_input(inputs)

        self.assertTrue(result, err)

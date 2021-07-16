import unittest

from parameterized import parameterized_class

from pyfx import Controller
from pyfx.config import parse
from pyfx.model import DataSourceType
from tests.fixtures import FIXTURES_DIR
from tests.fixtures.keys import split


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class AutoCompleteIT(unittest.TestCase):

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

        controller = Controller(self.config)
        model = controller._model
        model.load(DataSourceType.VARIABLE, data)
        view = controller._view

        inputs = split([
            self.keymap.json_browser.open_query_bar,  # enter query bar
            ".",  # input '.'
            self.keymap.autocomplete_popup.cursor_down,  # move down in the autocomplete popup
            self.keymap.autocomplete_popup.select,  # select option
            self.keymap.query_bar.query,  # apply query and switch to json browser
            self.keymap.exit  # exit
        ], self.keymap.global_command_key)

        result, err = view.process_input(data, inputs)
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

        controller = Controller(self.config)
        model = controller._model
        model.load(DataSourceType.VARIABLE, data)
        view = controller._view

        inputs = split([
            self.keymap.json_browser.open_query_bar,  # enter query bar
            ".",  # input '.'
            self.keymap.autocomplete_popup.cursor_down,  # move down in the autocomplete popup
            self.keymap.autocomplete_popup.cursor_down,
            self.keymap.autocomplete_popup.cursor_up,  # move up in the autocomplete popup
            self.keymap.autocomplete_popup.cancel,  # cancel autocomplete
            "backspace",  # remove last '.'
            self.keymap.query_bar.query,  # apply query and switch to json browser
            self.keymap.exit  # exit
        ], self.keymap.global_command_key)
        result, err = view.process_input(data, inputs)

        self.assertEqual(True, result, err)

    def test_autocomplete_navigation(self):
        """
        Test navigation in auto-complete, particularly with pressing navigation key
        at the start or end of the list.
        """
        data = {
            "alice": "0",
            "bob": "1"
        }

        controller = Controller(self.config)
        model = controller._model
        model.load(DataSourceType.VARIABLE, data)
        view = controller._view

        inputs = split([
            self.keymap.json_browser.open_query_bar,  # enter query bar
            ".",  # input '.'
            self.keymap.autocomplete_popup.cursor_down,  # move down in the autocomplete popup
            self.keymap.autocomplete_popup.cursor_down,
            self.keymap.autocomplete_popup.cursor_down,  # extra navigation key should not close the popup
            self.keymap.autocomplete_popup.cursor_up,  # move up in the autocomplete popup
            self.keymap.autocomplete_popup.cursor_up,
            self.keymap.autocomplete_popup.cursor_up,  # extra navigation key should not close the popup
            self.keymap.autocomplete_popup.cursor_up,  # extra navigation key should not close the popup
            self.keymap.autocomplete_popup.select,  # select option
            self.keymap.query_bar.query,  # apply query and switch to json browser
            self.keymap.exit  # exit
        ], self.keymap.global_command_key)
        result, err = view.process_input(data, inputs)

        self.assertEqual(True, result, err)

    def test_autocomplete_pass_keypress(self):
        """
        Test autocomplete popup pass keypress to query bar and update itself.
        """
        data = {
            "alice": "0",
            "bob": "1"
        }

        controller = Controller(self.config)
        model = controller._model
        model.load(DataSourceType.VARIABLE, data)
        view = controller._view

        inputs = split([
            self.keymap.json_browser.open_query_bar,  # enter query bar
            ".",  # input '.'
            "a",  # input 'a'
            self.keymap.autocomplete_popup.select,  # select autocomplete
            self.keymap.query_bar.query,  # apply query and switch to json browser
            self.keymap.exit  # exit
        ], self.keymap.global_command_key)
        result, err = view.process_input(data, inputs)

        self.assertEqual(True, result, err)

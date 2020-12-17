import unittest

from pyfx import Controller
from pyfx.config import parse


class AutoCompleteIT(unittest.TestCase):

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

        config = parse()
        controller = Controller(config)
        model = controller._model
        model.load_from_variable(data)
        view = controller._view
        result, err = view.process_input(data, [
            ".",  # enter query bar
            ".",  # input '.'
            "down",  # move down in the autocomplete popup
            "enter",  # select option
            "enter",  # apply query and switch to json browser
            "q"  # exit
        ])
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

        config = parse()
        controller = Controller(config)
        model = controller._model
        model.load_from_variable(data)
        view = controller._view
        result, err = view.process_input(data, [
            ".",  # enter query bar
            ".",  # input '.'
            "down",  # move down in the autocomplete popup
            "down",
            "up",  # move up in the autocomplete popup
            "esc",  # cancel autocomplete
            "backspace",  # remove last '.'
            "enter",  # apply query and switch to json browser
            "q"  # exit
        ])
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

        config = parse()
        controller = Controller(config)
        model = controller._model
        model.load_from_variable(data)
        view = controller._view
        result, err = view.process_input(data, [
            ".",  # enter query bar
            ".",  # input '.'
            "down",  # move down in the autocomplete popup
            "down",
            "down",  # extra navigation key should not close the popup
            "up",  # move up in the autocomplete popup
            "up",
            "up",  # extra navigation key should not close the popup
            "up",  # extra navigation key should not close the popup
            "esc",  # cancel autocomplete
            "backspace",  # remove last '.'
            "enter",  # apply query and switch to json browser
            "q"  # exit
        ])
        self.assertEqual(True, result, err)

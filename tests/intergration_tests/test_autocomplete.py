import unittest

from pyfx import Controller
from pyfx.config import parse


class AutoCompleteTest(unittest.TestCase):

    @staticmethod
    def test_autocomplete_select():
        """
        Test select one auto-complete options.
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
        view.process_input(data, [
            ".",      # enter query bar
            ".",      # input '.'
            "down",   # move down in the autocomplete popup
            "enter",  # select option
            "enter",  # apply query and switch to json browser
            "q"       # exit
        ])

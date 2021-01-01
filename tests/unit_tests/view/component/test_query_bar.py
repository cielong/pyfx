import unittest
from unittest.mock import MagicMock

from parameterized import parameterized_class

from pyfx.config import parse
from pyfx.core import Controller
from tests.fixtures import FIXTURES_DIR


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class QueryWindowTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.components.query_window.QueryWindow`.
    """

    def setUp(self):
        self.config = parse(FIXTURES_DIR / self.config_file)
        self.keymap = self.config.view.keymap.mapping

    def test_query_on_enter(self):
        """
        test query window submit query to controller
        """

        controller = Controller(self.config)
        controller.query = MagicMock(return_value="")
        # turn off autocomplete popup
        controller.complete = MagicMock(return_value=(False, "", []))

        query_window = controller._view._frame._query_bar
        query_window.setup()

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query_bar.query)

        # verify
        self.assertEqual(5, controller.complete.call_count)
        controller.query.assert_called_once_with("$.test")

    def test_query_on_esc(self):
        """
        test query window submit query to controller
        """

        controller = Controller(self.config)
        controller.query = MagicMock(return_value="")
        # turn off autocomplete popup
        controller.complete = MagicMock(return_value=(False, "", []))

        query_window = controller._view._frame._query_bar
        query_window.setup()

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query_bar.cancel)

        # verify
        self.assertEqual(5, controller.complete.call_count)
        controller.query.assert_called_once_with("$.test")

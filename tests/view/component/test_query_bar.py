import unittest
from unittest.mock import MagicMock

from pyfx.config import ConfigurationParser
from pyfx.core import Controller
from pyfx.view.components import QueryBar


class QueryWindowTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.components.query_window.QueryWindow`.
    """

    def test_query_on_enter(self):
        """
        test query window submit query to controller
        """
        config = ConfigurationParser().parse()

        controller = Controller(config)
        controller.query = MagicMock()
        controller.complete = MagicMock(return_value=None)

        view_manager = controller._view
        keymapper = view_manager._keymapper.query_bar
        query_window = QueryBar(view_manager, controller, keymapper)
        query_window.setup()

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), 'enter')

        # verify
        self.assertEqual(5, controller.complete.call_count)
        controller.query.assert_called_once_with("$.test")

    def test_query_on_esc(self):
        """
        test query window submit query to controller
        """
        config = ConfigurationParser().parse()

        controller = Controller(config)
        controller.query = MagicMock()
        controller.complete = MagicMock(return_value=None)

        view_manager = controller._view
        keymapper = view_manager._keymapper.query_bar
        query_window = QueryBar(view_manager, controller, keymapper)
        query_window.setup()

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), 'esc')

        # verify
        self.assertEqual(5, controller.complete.call_count)
        controller.query.assert_called_once_with("$.test")

import unittest
from unittest.mock import MagicMock

from pyfx.core import Controller
from pyfx.view import View
from pyfx.view.components import QueryWindow


class QueryWindowTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.components.query_window.QueryWindow`.
    """

    def test_query_on_enter(self):
        """
        test query window submit query to controller
        """
        controller = Controller()
        controller.query = MagicMock()
        controller.complete = MagicMock(return_value=None)

        view_manager = View(controller)
        query_window = QueryWindow(view_manager, controller)
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
        controller = Controller()
        controller.query = MagicMock()
        controller.complete = MagicMock(return_value=None)

        view_manager = View(controller)
        query_window = QueryWindow(view_manager, controller)
        query_window.setup()

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), 'esc')

        # verify
        self.assertEqual(5, controller.complete.call_count)
        controller.query.assert_called_once_with("$.test")

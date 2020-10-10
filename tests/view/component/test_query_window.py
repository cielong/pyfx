import unittest
from unittest.mock import MagicMock

from pyfx.core import Controller
from pyfx.view.components.query_window import QueryWindow


class QueryWindowTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.components.query_window.QueryWindow`.
    """

    @staticmethod
    def test_query_callback():
        """
        test query window submit query to controller
        """
        controller = Controller()
        controller.query = MagicMock()
        query_window = QueryWindow(controller)

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), "enter")

        # verify
        controller.query.assert_called_once_with("$.test")

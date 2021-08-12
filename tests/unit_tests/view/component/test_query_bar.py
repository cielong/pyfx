import unittest

from asynctest import Mock, CoroutineMock
from parameterized import parameterized_class

from pyfx.config import parse
from pyfx.view import View
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
        self.config = parse(FIXTURES_DIR / self.config_file).view
        self.keymap = self.config.keymap.mapping

    @staticmethod
    def query_only_client(path, *args):
        if path == "query":
            return [1, 2, 3]
        elif path == "complete":
            return False, args[0], []
        else:
            raise ValueError("Path not defined.")

    def test_query_on_enter(self):
        """
        test query window submit query to controller
        """
        client = Mock()
        client.invoke = CoroutineMock(
            side_effect=QueryWindowTest.query_only_client
        )
        view = View(self.config, client)
        query_window = view._frame._query_bar
        query_window.setup()

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query_bar.query)

        # verify
        self.assertEqual(6, client.invoke.call_count)
        client.invoke.assert_called_with("query", "$.test")

    def test_query_on_esc(self):
        """
        test query window submit query to controller
        """
        client = Mock()
        client.invoke = CoroutineMock(
            side_effect=QueryWindowTest.query_only_client
        )
        view = View(self.config, client)
        query_window = view._frame._query_bar
        query_window.setup()

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query_bar.cancel)

        # verify
        self.assertEqual(6, client.invoke.call_count)
        client.invoke.assert_called_with("query", "$.test")

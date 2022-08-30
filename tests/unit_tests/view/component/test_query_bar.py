import asyncio
import unittest

from unittest.mock import Mock
from parameterized import parameterized_class

from pyfx.service.client import Client
from pyfx.view.view_mediator import ViewMediator

from pyfx.config import parse
from pyfx.view.components import QueryBar
from tests.fixtures import FIXTURES_DIR


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class QueryWindowTest(unittest.TestCase):
    """
    Unit tests for :py:class:`pyfx.view.components.query_bar.QueryBar`.
    """

    def setUp(self):
        self.config = parse(FIXTURES_DIR / self.config_file).view
        self.keymap = self.config.keymap.mapping

    @staticmethod
    def invoke(path, *args):
        if path == "query":
            return [1, 2, 3]
        else:
            raise ValueError("Path not defined.")

    @staticmethod
    def invoke_with_timeout(timeout, path, *args):
        if path == "complete":
            return False, args[0], []
        else:
            raise ValueError("Path not defined.")

    def test_query_complete_timeout(self):
        """
        Test query bar submit query.
        """
        client = Client(None, None)

        def timeout(timeout, path, *args):
            raise asyncio.TimeoutError()
        client.invoke_with_timeout = Mock(side_effect=timeout)

        client.invoke = Mock(side_effect=QueryWindowTest.invoke)
        mediator = ViewMediator()
        query_window = QueryBar(mediator, client,
                                self.config.keymap.mapping.query_bar)

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query_bar.query)

        # verify
        self.assertEqual(5, client.invoke_with_timeout.call_count)
        client.invoke.assert_called_with("query", "$.test")

    def test_query_on_enter(self):
        """
        Test query bar submit query.
        """
        client = Client(None, None)
        client.invoke_with_timeout = Mock(
            side_effect=QueryWindowTest.invoke_with_timeout)
        client.invoke = Mock(side_effect=QueryWindowTest.invoke)
        mediator = ViewMediator()
        query_window = QueryBar(mediator, client,
                                self.config.keymap.mapping.query_bar)

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query_bar.query)

        # verify
        self.assertEqual(5, client.invoke_with_timeout.call_count)
        client.invoke.assert_called_with("query", "$.test")

    def test_query_on_esc(self):
        """
        Test query window submit query.
        """
        client = Client(None, None)
        client.invoke_with_timeout = Mock(
            side_effect=QueryWindowTest.invoke_with_timeout)
        client.invoke = Mock(side_effect=QueryWindowTest.invoke)
        mediator = ViewMediator()
        query_window = QueryBar(mediator, client,
                                self.config.keymap.mapping.query_bar)

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query_bar.cancel)

        # verify
        self.assertEqual(5, client.invoke_with_timeout.call_count)
        client.invoke.assert_called_with("query", "$.test")

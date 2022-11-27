import asyncio
import unittest
from unittest.mock import Mock

from parameterized import parameterized_class

from pyfx.config import keymaps_path
from pyfx.config import parse
from pyfx.config.config_parser import load
from pyfx.service.client import Client
from pyfx.view.components import QueryBar
from pyfx.view.keys import KeyMapper
from pyfx.view.view_mediator import ViewMediator
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
        self.config = parse(FIXTURES_DIR / self.config_file).ui
        self.keymap_config = keymaps_path / f"{self.config.keymap.mode}.yml"
        self.keymap = load(self.keymap_config, KeyMapper.query_bar)

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

        def func(timeout, path, *args):
            raise asyncio.TimeoutError()

        client.invoke_with_timeout = Mock(side_effect=func)

        client.invoke = Mock(side_effect=QueryWindowTest.invoke)
        mediator = ViewMediator()
        query_window = QueryBar(mediator, client, self.keymap)

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query)

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
        query_window = QueryBar(mediator, client, self.keymap)

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.query)

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
        query_window = QueryBar(mediator, client, self.keymap)

        # act
        for char in ".test":
            query_window.keypress((18,), char)
        query_window.keypress((18,), self.keymap.cancel)

        # verify
        self.assertEqual(5, client.invoke_with_timeout.call_count)
        client.invoke.assert_called_with("query", "$.test")

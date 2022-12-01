import unittest
from unittest.mock import Mock

from parameterized import parameterized_class

from pyfx.config import keymaps_path
from pyfx.config import parse
from pyfx.config.config_parser import load
from pyfx.service.client import Client
from pyfx.view.components import SavingBar
from pyfx.view.keyboards import KeyMapper
from pyfx.view.view_mediator import ViewMediator
from tests.fixtures import FIXTURES_DIR


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class SavingBarTest(unittest.TestCase):
    """Unit tests for :class:`pyfx.view.components.SavingBar`."""

    def setUp(self):
        self.config = parse(FIXTURES_DIR / self.config_file).ui
        self.keymap_config = keymaps_path / f"{self.config.keymap.mode}.yml"
        self.keymap = load(self.keymap_config, KeyMapper).saving_bar

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

    def test_save_on_enter(self):
        """
        Test query bar submit query.
        """
        client = Client(None, None)
        client.invoke_with_timeout = Mock(
            side_effect=SavingBarTest.invoke_with_timeout)
        client.invoke = Mock(side_effect=SavingBarTest.invoke)
        mediator = ViewMediator()
        saving_bar = SavingBar(self.keymap, client, mediator)

        # act
        for char in "test.json":
            saving_bar.keypress((18,), char)
        saving_bar.keypress((18,), self.keymap.save)

        # verify
        self.assertEqual(1, client.invoke.call_count)
        client.invoke.assert_called_with("save", "")

    def test_cancel_on_esc(self):
        """
        Test query window submit query.
        """
        client = Client(None, None)
        client.invoke_with_timeout = Mock(
            side_effect=SavingBarTest.invoke_with_timeout)
        client.invoke = Mock(side_effect=SavingBarTest.invoke)
        mediator = ViewMediator()
        saving_bar = SavingBar(self.keymap, client, mediator)

        # act
        for char in "test.json":
            saving_bar.keypress((18,), char)
        saving_bar.keypress((18,), self.keymap.cancel)

        # verify
        self.assertEqual(0, client.invoke.call_count)

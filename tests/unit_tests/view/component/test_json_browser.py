import unittest

from parameterized import parameterized_class
from urwid.compat import B

from pyfx.config import parse
from pyfx.config.config_parser import load
from pyfx.view.components import JSONBrowser
from pyfx.view.json_lib.json_node_factory import JSONNodeFactory
from pyfx.view.keys import KeyMapper
from pyfx.view.view_mediator import ViewMediator
from tests.fixtures import FIXTURES_DIR
from tests.fixtures.keys import split


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class JSONBrowserTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.components.view_window.ViewWindow`.
    """

    def setUp(self):
        self.config = parse(FIXTURES_DIR / self.config_file).ui
        self.keymap = load(self.config.keymap, KeyMapper)

    def test_json_browser_refresh(self):
        data = [
            {
                "key": "value"
            }
        ]
        mediator = ViewMediator()
        node_factory = JSONNodeFactory()
        json_browser = JSONBrowser(node_factory, mediator,
                                   self.keymap.json_browser)

        json_browser.refresh_view(data)
        content = json_browser.render((18, 3)).content()
        texts_before_refresh = [[t[2] for t in row] for row in content]

        # refresh view window by setting the top node
        new_data = {
            "key": "value"
        }
        json_browser.refresh_view(new_data)
        content = json_browser.render((18, 3)).content()
        texts_after_refresh = [[t[2] for t in row] for row in content]

        # verify
        self.assertTrue(texts_before_refresh != texts_after_refresh)
        texts_before_refresh_expected = [
            [B("[                 ")],
            [B("   "), B("{\xe2\x80\xa6}            ")],
            [B("]                 ")],
        ]
        self.assertEqual(texts_before_refresh_expected, texts_before_refresh)
        texts_after_refresh_expected = [
            [B("{                 ")],
            [B("   "), B('"key"'), B(": "), B('"value"'), B(' ')],
            [B("}                 ")],
        ]
        self.assertEqual(texts_after_refresh_expected, texts_after_refresh)

    def test_json_browser_collapse_all_from_start_line(self):
        """
        test json browser collapse all nested nodes when press key.
        """
        data = {
            "key": {
                "key": 'val'
            }
        }

        mediator = ViewMediator()
        node_factory = JSONNodeFactory()
        json_browser = JSONBrowser(node_factory, mediator,
                                   self.keymap.json_browser)

        json_browser.refresh_view(data)
        size = (18, 5)

        for key in split(self.keymap.json_browser.collapse_all,
                         self.keymap.global_command_key):
            json_browser.keypress(size, key)

        content = [[t[2] for t in row]
                   for row in json_browser.render(size).content()]

        # verify
        expected = [
            [B("{\xe2\x80\xa6}               ")],
            [B("                  ")],
            [B("                  ")],
            [B("                  ")],
            [B("                  ")]
        ]
        self.assertEqual(expected, content)

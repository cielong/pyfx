import unittest

from parameterized import parameterized_class
from urwid.compat import B

from pyfx import Controller
from pyfx.config import parse
from tests.fixtures import FIXTURES_DIR


@parameterized_class([
    {"config_file": "configs/basic.yml"},
    {"config_file": "configs/emacs.yml"},
    {"config_file": "configs/vim.yml"}
])
class ViewWindowTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.components.view_window.ViewWindow`.
    """

    def setUp(self):
        self.config = parse(FIXTURES_DIR / self.config_file)

    def test_view_window_refresh(self):
        data = [
            {
                "key": "value"
            }
        ]
        controller = Controller(self.config)
        json_browser = controller._view._frame._json_browser  # grab JSONBrowser instance to test

        json_browser.set_top_node(data)
        content = json_browser.render((18, 3)).content()
        texts_before_refresh = [[t[2] for t in row] for row in content]

        # refresh view window by setting the top node
        new_data = {
            "key": "value"
        }
        json_browser.set_top_node(new_data)
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

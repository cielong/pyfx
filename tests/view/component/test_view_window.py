import unittest

from pyfx.view.components.view_window import ViewWindow
from urwid.compat import B


class ViewWindowTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.components.view_window.ViewWindow`.
    """

    def test_view_window_refresh(self):
        data = [
            {
                "key": "value"
            }
        ]

        view_window = ViewWindow(data)

        # expand the first line
        content = view_window.render((18, 3)).content()
        texts_before_refresh = [[t[2] for t in row] for row in content]

        # refresh view window
        new_data = {
            "key": "value"
        }
        view_window.set_top_node(new_data)
        content = view_window.render((18, 3)).content()
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
            [B("   "), B("key: value     ")],
            [B("}                 ")],
        ]
        self.assertEqual(texts_after_refresh_expected, texts_after_refresh)

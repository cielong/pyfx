import unittest

from urwid.compat import B

from pyfx.ui.json_listbox import JSONListBox
from pyfx.ui.json_listwalker import JSONListWalker
from pyfx.ui.models.object_node import ObjectNode


class JSONListBoxTest(unittest.TestCase):

    def test_list_box_with_simple_object(self):
        """ test listbox rendering simple object with collapse pressing key `enter` and
        moving focus with pressing key `ctrl n`.
        """
        data = {
            "key": "value"
        }
        node = ObjectNode("", data, display_key=False)

        # act
        walker = JSONListWalker(start_from=node)
        listbox = JSONListBox(walker)

        contents_after_enter = [listbox.render((18, 2)).content()]
        contents = []
        prev_widget = None
        cur_widget, _ = listbox.get_focus()
        while prev_widget != cur_widget:
            contents.append(cur_widget.render((18,)).content())
            if cur_widget.is_expandable():
                listbox.keypress((18, 18), "enter")
                contents_after_enter.append(listbox.render((18, 2)).content())
            listbox.keypress((18, 18), "ctrl n")
            prev_widget = cur_widget
            cur_widget, _ = listbox.get_focus()

        texts = [[[t[2] for t in row] for row in content] for content in contents]
        texts_after_enter = [[[t[2] for t in row] for row in content] for content in contents_after_enter]

        # verify
        # verify that the last enter should expand all of the lines
        self.assertEqual(2, len(texts_after_enter))
        expected = [
            [B("                  ")],
            [B("   "), B("key: value     ")],
        ]
        self.assertEqual(expected, texts_after_enter[-1])

        # verify that after moving to the end, all the expandable lines have been expanded
        self.assertEqual(2, len(texts))
        expected = [
            [[B("                  ")]],
            [[B("   "), B("key: value     ")]],
        ]
        self.assertEqual(expected, texts)

    def test_list_box_with_nested_object(self):
        """ test listbox rendering nested object with collapse pressing key `enter` and
        moving focus with pressing key `ctrl n`.
        """
        data = {
            "key": {
                "nested_key": "value"
            }
        }
        node = ObjectNode("", data, display_key=False)

        # act
        walker = JSONListWalker(start_from=node)
        listbox = JSONListBox(walker)

        contents_after_enter = [listbox.render((18, 4)).content()]
        contents = []
        prev_widget = None
        cur_widget, _ = listbox.get_focus()
        while prev_widget != cur_widget:
            contents.append(cur_widget.render((18,)).content())
            if cur_widget.is_expandable():
                listbox.keypress((18, 18), "enter")
                contents_after_enter.append(listbox.render((18, 4)).content())
            listbox.keypress((18, 18), "ctrl n")
            prev_widget = cur_widget
            cur_widget, _ = listbox.get_focus()

        texts = [[[t[2] for t in row] for row in content] for content in contents]
        texts_after_enter = [[[t[2] for t in row] for row in content] for content in contents_after_enter]

        # verify
        # verify that the last enter should expand all of the lines
        self.assertEqual(3, len(texts_after_enter))
        expected = [
            [B("                  ")],
            [B("   "), B("key:           ")],
            [B("      "), B("nested_key: ")],
            [B("      "), B("value       ")]
        ]
        self.assertEqual(expected, texts_after_enter[-1])

        # verify that after moving to the end, all the expandable lines have been expanded
        self.assertEqual(3, len(texts))
        expected = [
            [[B("                  ")]],
            [[B("   "), B("key:           ")]],
            [[B("      "), B("nested_key: ")],
             [B("      "), B("value       ")]]
        ]
        self.assertEqual(expected, texts)

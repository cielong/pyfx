import unittest

from urwid.compat import B

from pyfx.view.json_lib.json_listbox import JSONListBox
from pyfx.view.json_lib.json_listwalker import JSONListWalker
from pyfx.view.json_lib.node_factory import NodeFactory


class JSONListBoxTest(unittest.TestCase):

    def test_list_box_with_simple_object(self):
        """
        test listbox rendering simple object with collapse pressing key `enter` and
        moving focus with pressing key `ctrl n`.
        """
        data = {
            "key": "value"
        }
        node = NodeFactory.create_node("", data, parent=None, display_key=False)

        # act
        walker = JSONListWalker(start_from=node)
        listbox = JSONListBox(walker)

        contents = []
        prev_widget, prev_node = None, None
        cur_widget, cur_node = listbox.get_focus()
        while prev_widget != cur_widget:
            if not cur_node.is_expanded():
                listbox.keypress((18, 18), "enter")
                cur_widget, cur_node = listbox.get_focus()
            contents.append(cur_widget.render((18,)).content())
            listbox.keypress((18, 18), "ctrl n")
            prev_widget, prev_node = cur_widget, cur_node
            cur_widget, cur_node = listbox.get_focus()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        # verify that after moving to the end, all the expandable lines have been expanded
        self.assertEqual(3, len(texts))
        expected = [
            [[B("{                 ")]],
            [[B("   "), B("key: value     ")]],
            [[B("}                 ")]],
        ]
        self.assertEqual(expected, texts)

    def test_list_box_with_nested_object(self):
        """
        test listbox rendering nested object with collapse pressing key `enter` and
        moving focus with pressing key `ctrl n`.
        """
        data = {
            "key": {
                "nested_key": "value"
            }
        }
        node = NodeFactory.create_node("", data, parent=None, display_key=False)

        # act
        walker = JSONListWalker(start_from=node)
        listbox = JSONListBox(walker)

        contents_after_enter = [listbox.render((18, 4)).content()]
        contents = []
        prev_widget, prev_node = None, None
        cur_widget, cur_node = listbox.get_focus()
        while prev_widget != cur_widget:
            if not cur_node.is_expanded():
                listbox.keypress((18, 18), "enter")
                cur_widget, cur_node = listbox.get_focus()
            contents.append(cur_widget.render((18,)).content())
            listbox.keypress((18, 18), "ctrl n")
            prev_widget, prev_node = cur_widget, cur_node
            cur_widget, cur_node = listbox.get_focus()

        texts = [[[t[2] for t in row] for row in content] for content in contents]
        texts_after_enter = [[[t[2] for t in row] for row in content] for content in contents_after_enter]

        # verify
        # verify that after moving to the end, all the expandable lines have been expanded
        self.assertEqual(5, len(texts))
        expected = [
            [[B("{                 ")]],
            [[B("   "), B("key: {         ")]],
            [[B("      "), B("nested_key: ")],
             [B("      "), B("value       ")]],
            [[B("   "), B("}              ")]],
            [[B("}                 ")]],
        ]
        self.assertEqual(expected, texts)

import unittest

from urwid.compat import B

from pyfx.view.json_lib.models.object_node import ObjectNode


class ObjectNodeTest(unittest.TestCase):

    def test_simple_dict(self):
        """ test rendering of a not-nested JSON object """
        data = {
            "key": "value"
        }

        # act
        node = ObjectNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(2, len(texts))
        expected = [
            [[B("                  ")]],
            [[B("   "), B("key: value     ")]]
        ]
        self.assertEqual(expected, texts)

    def test_nested_dict(self):
        """ test rendering of a nested JSON object """
        data = {
            "key": {
                "nested_key": "value"
            }
        }

        # act
        node = ObjectNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(3, len(texts))
        expected = [
            [[B("                  ")]],
            [[B("   "), B("key:           ")]],
            [[B("      "), B("nested_key: ")],
             [B("      "), B("value       ")]]
        ]
        self.assertEqual(expected, texts)

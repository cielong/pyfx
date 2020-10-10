import unittest

from urwid.compat import B

from pyfx.view.json_lib.object.object_node import ObjectNode


class ObjectNodeTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.json_lib.object.object_node.ObjectNode`
    """

    def test_empty_object(self):
        """ test rendering of an empty JSON object"""
        data = {}

        # act
        node = ObjectNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), "enter")
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(2, len(texts))
        expected = [
            [[B("{                 ")]],
            [[B("}                 ")]],
        ]
        self.assertEqual(expected, texts)

    def test_simple_object(self):
        """ test rendering of a not-nested JSON object """
        data = {
            "key": "value"
        }

        # act
        node = ObjectNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), "enter")
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(3, len(texts))
        expected = [
            [[B("{                 ")]],
            [[B("   "), B("key: value     ")]],
            [[B("}                 ")]],
        ]
        self.assertEqual(expected, texts)

    def test_nested_object(self):
        """
        test rendering of a nested JSON object
        """

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
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), "enter")
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
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

    def test_object_with_list_child(self):
        """
        test rendering of a JSON object with list child
        """

        data = {
            "key": [
                1
            ]
        }

        # act
        node = ObjectNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), "enter")
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(5, len(texts))
        expected = [
            [[B("{                 ")]],
            [[B("   "), B("key: [         ")]],
            [[B("      "), B("1           ")]],
            [[B("   "), B("]              ")]],
            [[B("}                 ")]],
        ]
        self.assertEqual(expected, texts)

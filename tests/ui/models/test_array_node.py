import unittest

from urwid.compat import B

from pyfx.view.models.array_node import ArrayNode


class ArrayNodeTest(unittest.TestCase):
    def test_simple_array(self):
        """ test rendering a not-nested array """
        data = [
            1,
            2,
            "str"
        ]

        # act
        node = ArrayNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(4, len(texts))
        expected = [
            [[B("                  ")]],
            [[B("   "), B("1              ")]],
            [[B("   "), B("2              ")]],
            [[B("   "), B("str            ")]]
        ]
        self.assertEqual(expected, texts)

    def test_nested_array(self):
        """ test rendering a nested array """
        data = [
            1,
            2,
            [
                "str",
                True
            ]
        ]

        # act
        node = ArrayNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(6, len(texts))
        expected = [
            [[B("                  ")]],
            [[B("   "), B("1              ")]],
            [[B("   "), B("2              ")]],
            [[B("   "), B("               ")]],
            [[B("      "), B("str         ")]],
            [[B("      "), B("True        ")]],
        ]
        self.assertEqual(expected, texts)

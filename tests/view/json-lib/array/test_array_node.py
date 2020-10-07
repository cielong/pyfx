import unittest

from urwid.compat import B

from pyfx.view.json_lib.array.array_node import ArrayNode


class ArrayNodeTest(unittest.TestCase):
    def test_simple_array(self):
        """
        test rendering a not-nested array
        """

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
            [[B("[                 ")]],
            [[B("   "), B("1              ")]],
            [[B("   "), B("2              ")]],
            [[B("   "), B("str            ")]],
            [[B("]                 ")]]
        ]
        self.assertEqual(expected, texts)

    def test_nested_array(self):
        """
        test rendering a nested array
        """

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
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), "enter")
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(8, len(texts))
        expected = [
            [[B("[                 ")]],
            [[B("   "), B("1              ")]],
            [[B("   "), B("2              ")]],
            [[B("   "), B("[              ")]],
            [[B("      "), B("str         ")]],
            [[B("      "), B("True        ")]],
            [[B("   "), B("]              ")]],
            [[B("]                 ")]]
        ]
        self.assertEqual(expected, texts)

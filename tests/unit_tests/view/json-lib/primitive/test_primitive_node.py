import unittest

from pyfx.view.json_lib import NodeFactory
from urwid.compat import B


class AtomicNodeTest(unittest.TestCase):
    """
    unit tests for :py:class:`pyfx.view.json_lib.primitive.primitive_node.PrimitiveNode`
    """

    def test_integer_node(self):
        """ test JSON `integer` rendering """
        data = 1

        # act
        node = NodeFactory.create_node('', data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), 'enter')
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B('1'), B('                 ')]]
        ]
        self.assertEqual(expected, texts)

    def test_numeric_node(self):
        """ test JSON `numeric` rendering """
        data = 1.0

        # act
        node = NodeFactory.create_node("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), 'enter')
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B('1.0'), B('               ')]]
        ]
        self.assertEqual(expected, texts)

    def test_string_node(self):
        """ test JSON `string` rendering """

        data = 'str'

        # act
        node = NodeFactory.create_node('', data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), 'enter')
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B('"str"'), B('             ')]]
        ]
        self.assertEqual(expected, texts)

    def test_boolean_node(self):
        """ test JSON `boolean` rendering """

        data = True

        # act
        node = NodeFactory.create_node("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), 'enter')
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B('true'), B('              ')]]
        ]
        self.assertEqual(expected, texts)

    def test_null_node(self):
        """ test JSON `null` rendering """

        data = None

        # act
        node = NodeFactory.create_node('', data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                widget.keypress((18,), 'enter')
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B('null'), B('              ')]]
        ]
        self.assertEqual(expected, texts)

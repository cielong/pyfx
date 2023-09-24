import json
import unittest

from pyfx.view.json_lib.json_node_factory import JSONNodeFactory


class ObjectNodeTest(unittest.TestCase):
    """
    Unit tests for :py:class:`pyfx.view.json_lib.object.object_node.ObjectNode`.
    """

    def setUp(self):
        self._node_factory = JSONNodeFactory()

    def test_order(self):
        """
        Test that the key order is maintained after rendering.
        """
        # Create a JSON string that has non-alphabetical ordered keys
        serialized_json = """
        {
          "name": "John",
          "age": 28
        }
        """
        data = json.loads(serialized_json)

        # act
        node = self._node_factory.create_root_node(data)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                node.toggle_expanded()
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content]
                 for content in contents]

        # verify
        self.assertEqual(4, len(texts))
        expected = [
            [[b'{                 ']],
            [[b'   ', b'"name"', b': ', b'"John"', b' ']],
            [[b'   ', b'"age"', b': ', b'28', b'      ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)

    def test_empty_object(self):
        """
        Test rendering of an empty JSON object.
        """
        data = {}

        # act
        node = self._node_factory.create_root_node(data)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                node.toggle_expanded()
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        # restart and scan from the end widget
        node = self._node_factory.create_root_node(data)
        widget = node.get_end_node().get_widget()
        contents_from_end = []
        while widget is not None:
            contents_from_end.append(widget.render((18,)).content())
            widget = widget.prev_inorder()

        texts = [[[t[2] for t in row] for row in content]
                 for content in contents]
        texts_from_end = [[[t[2] for t in row]
                           for row in content] for content in contents_from_end]
        texts_from_end.reverse()

        # verify
        self.assertEqual(2, len(texts))
        expected = [
            [[b'{                 ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)
        self.assertEqual(expected, texts_from_end)

    def test_simple_object(self):
        """
        Test rendering of a not-nested JSON object.
        """
        data = {
            "k1": "v1",
            "k2": "v2"
        }

        # act
        node = self._node_factory.create_root_node(data)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                node.toggle_expanded()
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content]
                 for content in contents]

        # verify
        self.assertEqual(4, len(texts))
        expected = [
            [[b'{                 ']],
            [[b'   ', b'"k1"', b': ', b'"v1"', b'     ']],
            [[b'   ', b'"k2"', b': ', b'"v2"', b'     ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)

    def test_nested_object(self):
        """
        Test rendering of a nested JSON object.
        """

        data = {
            "key": {
                "key": "val"
            }
        }

        # act
        node = self._node_factory.create_root_node(data)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                node.toggle_expanded()
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content]
                 for content in contents]

        # verify
        self.assertEqual(5, len(texts))
        expected = [
            [[b'{                 ']],
            [[b'   ', b'"key"', b': ', b'{       ']],
            [[b'      ', b'"key"', b': ', b'"val"']],
            [[b'   ', b'}              ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)

    def test_object_with_list_child(self):
        """
        Test rendering of a JSON object with list child.
        """

        data = {
            "key": [
                1
            ]
        }

        # act
        node = self._node_factory.create_root_node(data)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            node = widget.get_node()
            if not node.is_expanded():
                node.toggle_expanded()
            widget = node.get_widget()
            contents.append(widget.render((18,)).content())
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content]
                 for content in contents]

        # verify
        self.assertEqual(5, len(texts))
        expected = [
            [[b'{                 ']],
            [[b'   ', b'"key"', b': ', b'[       ']],
            [[b'      ', b'1', b'           ']],
            [[b'   ', b']              ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)

    def test_prev_order(self):
        data = {
            "k1": "v1",
            "k2": "v2"
        }

        node = self._node_factory.create_root_node(data)
        # start from the end
        widget = node.get_end_node().get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            widget = widget.prev_inorder()

        texts = [[[t[2] for t in row] for row in content]
                 for content in contents]
        texts.reverse()

        # verify
        self.assertEqual(4, len(texts))
        expected = [
            [[b'{                 ']],
            [[b'   ', b'"k1"', b': ', b'"v1"', b'     ']],
            [[b'   ', b'"k2"', b': ', b'"v2"', b'     ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)

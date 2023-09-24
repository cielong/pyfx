import unittest

from pyfx.view.json_lib.json_node_factory import JSONNodeFactory
from tests.fixtures.test_class import TestClass
from tests.fixtures.test_class import TestClassNodeCreator


class NodeFactoryTest(unittest.TestCase):

    def setUp(self):
        self._node_factory = JSONNodeFactory()

    def test_render_user_defined_class(self):
        data = TestClass(1, "test", True)

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
            [[b'   ', b'"_id"', b': ', b'1', b'       ']],
            [[b'   ', b'"_name"', b': ', b'"test"']],
            [[b'   ', b'"_flag"', b': ', b'true', b'  ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)

    def test_render_user_defined_class_with_customized_widget(self):
        self._node_factory.register(TestClassNodeCreator(self._node_factory))
        data = TestClass(1, "test", True)

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
            [[b'   ', b'"id"', b': ', b'1', b'        ']],
            [[b'   ', b'"name"', b': ', b'"test"', b' ']],
            [[b'   ', b'"flag"', b': ', b'true', b'   ']],
            [[b'}                 ']],
        ]
        self.assertEqual(expected, texts)

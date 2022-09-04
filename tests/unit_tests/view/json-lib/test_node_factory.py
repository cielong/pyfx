import unittest

from urwid.compat import B

from pyfx.view.json_lib import JSONNodeFactory
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
            [[B("{                 ")]],
            [[B("   "), B('"_id"'), B(": "), B('1'), B('       ')]],
            [[B("   "), B('"_name"'), B(": "), B('"test"')]],
            [[B("   "), B('"_flag"'), B(": "), B('true'), B('  ')]],
            [[B("}                 ")]],
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
            [[B("{                 ")]],
            [[B("   "), B('"id"'), B(": "), B('1'), B('        ')]],
            [[B("   "), B('"name"'), B(": "), B('"test"'), B(' ')]],
            [[B("   "), B('"flag"'), B(": "), B('true'), B('   ')]],
            [[B("}                 ")]],
        ]
        self.assertEqual(expected, texts)

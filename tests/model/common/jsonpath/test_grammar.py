import unittest

from antlr4 import *
from pyfx.model.common.jsonpath.JSONPathLexer import JSONPathLexer
from pyfx.model.common.jsonpath.JSONPathParser import JSONPathParser


class TestGrammar(unittest.TestCase):
    def test_root(self):
        tree = self._parse("$")
        print(tree.toStringTree())

    def test_dot_wildcard(self):
        tree = self._parse("$.*")
        print(tree.toStringTree())

    def test_dot_child(self):
        tree = self._parse("$.child")
        print(tree.toStringTree())

    def test_bracket_child(self):
        tree = self._parse("$['child']")
        print(tree.toStringTree())

    def test_bracket_wildcard(self):
        tree = self._parse("$['*']")
        print(tree.toStringTree())

    def test_bracket_space(self):
        tree = self._parse("$['first child']")
        print(tree.toStringTree())

    def test_dot_bracket_child(self):
        tree = self._parse("$.['child']")
        print(tree.toStringTree())

    def test_array_slice(self):
        tree = self._parse("$[0:2:1]")
        print(tree.toStringTree())

    def test_array_slice_no_step(self):
        tree = self._parse("$[0:2]")
        print(tree.toStringTree())

    def test_array_slice_no_start(self):
        tree = self._parse("$[:2:1]")
        print(tree.toStringTree())

    def test_array_slice_no_start_and_step(self):
        tree = self._parse("$[:2]")
        print(tree.toStringTree())

    def test_array_slice_no_end(self):
        tree = self._parse("$[0::1]")
        print(tree.toStringTree())

    def test_array_slice_no_end_and_step(self):
        tree = self._parse("$[0:]")
        print(tree.toStringTree())

    def test_array_index(self):
        tree = self._parse("$[0]")
        print(tree.toStringTree())

    def test_dot_array_index(self):
        tree = self._parse("$.[0]")
        print(tree.toStringTree())

    def test_union_index(self):
        tree = self._parse("$[0, 1, 2]")
        print(tree.toStringTree())

    def test_union_child_name(self):
        tree = self._parse("$['first_child', 'second_child']")
        print(tree.toStringTree())

    def test_filter_string(self):
        tree = self._parse("$[?(@.child == 'test')]")
        print(tree.toStringTree())

    def test_filter_numeric_greater(self):
        tree = self._parse("$[?(@.child > 1)]")
        print(tree.toStringTree())

    def test_filter_numeric_equal(self):
        tree = self._parse("$[?(@.child == 1)]")
        print(tree.toStringTree())

    def test_filter_numeric_less(self):
        tree = self._parse("$[?(@.child < 1)]")
        print(tree.toStringTree())

    def test_filter_boolean(self):
        tree = self._parse("$[?(@.child)]")
        print(tree.toStringTree())

    def test_length(self):
        tree = self._parse("$[(@.length - 1)]")
        print(tree.toStringTree())

    @staticmethod
    def _parse(input):
        input_stream = InputStream(input)
        lexer = JSONPathLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JSONPathParser(stream)
        return parser.jsonpath()

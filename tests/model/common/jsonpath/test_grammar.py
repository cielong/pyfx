import unittest

from antlr4 import *

from pyfx.model.common.jsonpath.JSONPathLexer import JSONPathLexer
from pyfx.model.common.jsonpath.JSONPathParser import JSONPathParser


class TestGrammar(unittest.TestCase):
    def test_root(self):
        self.parse("$")

    def test_dot_wildcard(self):
        self.parse("$.*")

    def test_dot_child(self):
        self.parse("$.child")

    def test_bracket_child(self):
        self.parse("$['child']")

    def test_bracket_wildcard(self):
        self.parse("$[*]")

    def test_bracket_space(self):
        self.parse("$['first child']")

    def test_dot_bracket_child(self):
        self.parse("$.['child']")

    def test_array_slice(self):
        self.parse("$[0:2:1]")

    def test_array_slice_no_step(self):
        self.parse("$[0:2]")

    def test_array_slice_no_start(self):
        self.parse("$[:2:1]")

    def test_array_slice_no_start_and_step(self):
        self.parse("$[:2]")

    def test_array_slice_no_end(self):
        self.parse("$[0::1]")

    def test_array_slice_no_end_and_step(self):
        self.parse("$[0:]")

    def test_array_index(self):
        self.parse("$[0]")

    def test_dotted_array_index(self):
        self.parse("$.[0]")

    def test_union_child_name(self):
        self.parse("$['first_child', 'second_child']")

    def test_filter_string(self):
        self.parse("$[?(@.child == 'test')]")

    def test_filter_numeric_greater(self):
        self.parse("$[?(@.child > 1)]")

    def test_filter_numeric_equal(self):
        self.parse("$[?(@.child == 1)]")

    def test_filter_numeric_less(self):
        self.parse("$[?(@.child < 1)]")

    def test_filter_boolean(self):
        self.parse("$[?(@.child)]")

    @staticmethod
    def parse(input):
        input_stream = InputStream(input)
        lexer = JSONPathLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JSONPathParser(stream)
        parser.jsonpath()

import unittest

from pyfx.model.common import Parser


class TestParser(unittest.TestCase):
    def test_tokenize_with_empty_string(self):
        parser = Parser()

        tokens = parser._tokenize("")

        self.assertEqual([], tokens)

    def test_tokenize_with_root(self):
        parser = Parser()

        tokens = parser._tokenize("$")

        self.assertEqual(['$'], tokens)

    def test_tokenize_with_dot(self):
        parser = Parser()

        tokens = parser._tokenize("...")

        self.assertEqual(['...'], tokens)

    def test_tokenize_with_dot_end(self):
        parser = Parser()

        tokens = parser._tokenize("$.")

        self.assertEqual(['$', '.'], tokens)

    def test_tokenize_with_dot_style(self):
        parser = Parser()

        tokens = parser._tokenize("$.t")

        self.assertEqual(['$', '.', 't'], tokens)

    def test_tokenize_with_invalid_dot(self):
        parser = Parser()

        tokens = parser._tokenize("$...")

        self.assertEqual(['$', '...'], tokens)

    def test_tokenize_with_double_dot(self):
        parser = Parser()

        tokens = parser._tokenize("$..")

        self.assertEqual(['$', '..'], tokens)

    def test_tokenize_with_double_dot_and_incomplete_token(self):
        parser = Parser()

        tokens = parser._tokenize("$..t")

        self.assertEqual(['$', '..', 't'], tokens)

    def test_tokenize_with_brackets_style(self):
        parser = Parser()

        tokens = parser._tokenize("$['t")

        self.assertEqual(['$', "['t"], tokens)

    def test_tokenize_with_brackets_closed(self):
        parser = Parser()

        tokens = parser._tokenize("$['query']")

        self.assertEqual(['$', "['query']"], tokens)

    def test_tokenize_with_brackets_closed_and_dot(self):
        parser = Parser()

        tokens = parser._tokenize("$['query'].")

        self.assertEqual(['$', "['query']", '.'], tokens)

    def test_tokenize_with_direct_filters(self):
        parser = Parser()

        tokens = parser._tokenize("$[?(!@.isbn)]")

        self.assertEqual(['$', "[?(!@.isbn)]"], tokens)

    def test_tokenize_with_direct_expression(self):
        parser = Parser()

        tokens = parser._tokenize("$[@.length - 1]")

        self.assertEqual(['$', "[@.length - 1]"], tokens)

    def test_tokenize_with_array_expression(self):
        parser = Parser()

        tokens = parser._tokenize("$.array[*]")

        self.assertEqual(['$', '.', 'array', '[*]'], tokens)

    def test_tokenize_with_filter_expression(self):
        parser = Parser()

        tokens = parser._tokenize("$.store.book[?(@.price < 10)]")

        self.assertEqual(['$', '.', 'store', '.', 'book', '[?(@.price < 10)]'], tokens)

    def test_tokenize_with_array_in_filter_expression(self):
        parser = Parser()

        tokens = parser._tokenize("$.book[?(@.price[0] < 10)]")

        self.assertEqual(['$', '.', 'book', '[?(@.price[0] < 10)]'], tokens)

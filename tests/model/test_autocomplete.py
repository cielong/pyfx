import unittest

from pyfx.model.autocomplete import JSONPathAutoComplete


class TestAutoComplete(unittest.TestCase):

    def test_tokenize_with_root(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$")

        self.assertEqual(['$'], tokens)

    def test_tokenize_with_dot_end(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$.")

        self.assertEqual(['$', ''], tokens)

    def test_tokenize_with_dot_style(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$.t")

        self.assertEqual(['$', 't'], tokens)

    def test_tokenize_with_double_dot(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$..")

        self.assertEqual(['$', ''], tokens)

    def test_tokenize_with_double_dot_and_incomplete_token(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$..t")

        self.assertEqual(['$', 't'], tokens)

    def test_tokenize_with_brackets_style(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$['t")

        self.assertEqual(['$', "['t"], tokens)

    def test_tokenize_with_brackets_closed(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$['query']")

        self.assertEqual(['$', "['query']", ''], tokens)

    def test_tokenize_with_array_expression(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$.array[*]")

        self.assertEqual(['$', 'array[*]', ''], tokens)

    def test_tokenize_with_filter_expression(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$.store.book[?(@.price < 10)]")

        self.assertEqual(['$', 'store', 'book[?(@.price < 10)]', ''], tokens)

    def test_tokenize_with_array_in_filter_expression(self):
        autocomplete = JSONPathAutoComplete()

        tokens = autocomplete._tokenize("$.book[?(@.price[0] < 10)]")

        self.assertEqual(['$', 'book[?(@.price[0] < 10)]', ''], tokens)


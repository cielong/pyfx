import unittest

from pyfx.model.autocomplete import JSONPathAutoComplete


class TestAutoComplete(unittest.TestCase):
    def test_complete_root(self):
        data = {
            'k1': 'v1'
        }

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, '$')

        self.assertEqual('', prefix)
        self.assertEqual(['k1'], options)

    def test_complete_root_with_dot(self):
        data = {
            'k1': 'v1'
        }

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, '$.')

        self.assertEqual('', prefix)
        self.assertEqual(['k1'], options)

    def test_complete_root_with_bracket(self):
        data = {
            'k1': 'v1'
        }

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, '$[')

        self.assertEqual('[', prefix)
        self.assertEqual(["['k1']"], options)

    def test_complete_root_with_bracket_quote(self):
        data = {
            'k1': 'v1'
        }

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, "$['")

        self.assertEqual("['", prefix)
        self.assertEqual(["['k1']"], options)

    def test_complete_root_with_bracket_quote_and_dot_key(self):
        data = {
            'k\'1': 'v1'
        }

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, "$['")

        self.assertEqual("['", prefix)
        self.assertEqual(["['k\'1']"], options)

    def test_complete_array_without_bracket(self):
        data = [
            "v1",
            "v2"
        ]

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, "$")

        self.assertEqual("", prefix)
        self.assertEqual(['[*]', '[0]', '[1]'], options)

    def test_complete_array_with_bracket(self):
        data = [
            "v1",
            "v2"
        ]

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, "$[")

        self.assertEqual("[", prefix)
        self.assertEqual(['[*]', '[0]', '[1]'], options)

    def test_complete_query(self):
        data = {
            "widget": {
                "debug": "on",
                "list": [1, 2, 3, 4],
            },
            "test": 50
        }

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, "$.widget.l")

        self.assertEqual("l", prefix)
        self.assertEqual(['list'], options)

    def test_complete_invalid_query(self):
        data = {
            "widget": {
                "debug": "on",
                "list": [1, 2, 3, 4],
            },
            "test": 50
        }

        autocomplete = JSONPathAutoComplete()
        (prefix, options) = autocomplete.complete(data, "$.widget['list']q")

        self.assertEqual("q", prefix)
        self.assertEqual(['list'], options)

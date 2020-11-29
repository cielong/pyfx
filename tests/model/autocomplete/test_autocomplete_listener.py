import unittest

from pyfx import Controller
from pyfx.model import Model
from pyfx.model.autocomplete import autocomplete


class AutoCompleteListenerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(Controller())

    def test_empty_string(self):
        _, options = autocomplete("", self.model.query)
        self.assertEqual(["$"], options)

    def test_single_dot(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$.", self.model.query)
        self.assertEqual(["*", "key"], options)

    def test_double_dot(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$..", self.model.query)
        self.assertEqual([], options)

    def test_invalid_dots(self):
        # invalid case
        _, options = autocomplete("$...", self.model.query)
        self.assertEqual([], options)

    def test_dot_incomplete_field(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$.k", self.model.query)
        self.assertEqual(["key"], options)

    def test_dot_complete_field(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$.key", self.model.query)
        self.assertEqual([".", "["], options)

    # bracket
    def test_open_bracket(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$[", self.model.query)
        self.assertEqual(["[*]", "['key']"], options)

    def test_dotted_open_bracket(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$.[", self.model.query)
        self.assertEqual(["[*]", "['key']"], options)

    def test_incomplete_open_bracket(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$.['k", self.model.query)
        self.assertEqual(["['key']"], options)

    def test_complete_bracket_field(self):
        self.model.load_from_variable({
            "Alice's key": {
                "key": "value"
            }
        })
        _, options = autocomplete("$.['Alice\\\'s key']", self.model.query)
        self.assertEqual(['.', '['], options)

    def test_invalid_dotted_open_bracket(self):
        _, options = autocomplete("$...[", self.model.query)
        self.assertEqual([], options)

    def test_invalid_bracket(self):
        _, options = autocomplete("$[[", self.model.query)
        self.assertEqual([], options)

    def test_array_index(self):
        self.model.load_from_variable([
            "item1",
            "item2"
        ])
        _, options = autocomplete("$[", self.model.query)
        self.assertEqual(["[*]", "[0]", "[1]"], options)

    # filters
    def test_open_filter(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$[?(", self.model.query)
        self.assertEqual(["@.key"], options)

    def test_open_filter_with_only_question_mark(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$[?", self.model.query)
        self.assertEqual(["("], options)

    def test_dotted_open_filter(self):
        self.model.load_from_variable({
            "key": "value"
        })
        _, options = autocomplete("$.[?(", self.model.query)
        self.assertEqual(["@.key"], options)

    # union
    def test_incomplete_union_comma(self):
        self.model.load_from_variable({
            "k1": "v1",
            "k2": "v2"
        })
        _, options = autocomplete("$.['k1',", self.model.query)
        self.assertEqual(["'k2'"], options)

    def test_incomplete_union_second_key(self):
        self.model.load_from_variable({
            "k1": "v1",
            "k2": "v2"
        })
        _, options = autocomplete("$.['k1','", self.model.query)
        self.assertEqual(["'k2'"], options)

import unittest

from pyfx.model import Model
from pyfx.model.autocomplete import autocomplete


class AutoCompleteListenerTest(unittest.TestCase):
    def test_empty_string(self):
        self.model = Model()
        self.model.load("")
        _, _, options = autocomplete("", self.model.query)
        self.assertEqual(["$"], options)

    def test_single_dot(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$.", self.model.query)
        self.assertEqual(["*", "key"], options)

    def test_double_dot(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$..", self.model.query)
        self.assertEqual([], options)

    def test_invalid_dots(self):
        # invalid case
        self.model = Model()
        self.model.load("")
        _, _, options = autocomplete("$...", self.model.query)
        self.assertEqual([], options)

    def test_dot_incomplete_field(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$.k", self.model.query)
        self.assertEqual(["key"], options)

    def test_dot_incomplete_field_after_array_wildcard(self):
        self.model = Model()
        self.model.load([{"key": "v1"}, {"key": "v2"}])
        _, _, options = autocomplete("$[*].k", self.model.query)
        self.assertEqual(["key"], options)

    def test_dot_complete_field(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$.key", self.model.query)
        self.assertEqual([".", "["], options)

    def test_incomplete_single_dot_after_array_wildcard(self):
        self.model = Model()
        self.model.load([{"key": "v1"}, {"key": "v2"}])
        _, _, options = autocomplete("$[*].", self.model.query)
        self.assertEqual(["key"], options)

    # bracket
    def test_open_bracket(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$[", self.model.query)
        self.assertEqual(["[*]", "['key']"], options)

    def test_dotted_open_bracket(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$.[", self.model.query)
        self.assertEqual(["[*]", "['key']"], options)

    def test_incomplete_open_bracket(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$.['k", self.model.query)
        self.assertEqual(["['key']"], options)

    def test_complete_bracket_field(self):
        self.model = Model()
        self.model.load({"Alice's key": {"key": "value"}})
        _, _, options = autocomplete("$.['Alice\\'s key']", self.model.query)
        self.assertEqual([".", "["], options)

    def test_invalid_dotted_open_bracket(self):
        self.model = Model()
        self.model.load("")
        _, _, options = autocomplete("$...[", self.model.query)
        self.assertEqual([], options)

    def test_invalid_bracket(self):
        self.model = Model()
        self.model.load("")
        _, _, options = autocomplete("$[[", self.model.query)
        self.assertEqual([], options)

    def test_array_index(self):
        self.model = Model()
        self.model.load(["item1", "item2"])
        is_partial_complete, _, options = autocomplete("$[", self.model.query)
        self.assertEqual(["[*]", "[0]", "[1]"], options)
        self.assertFalse(is_partial_complete)

    def test_incomplete_bracket_field_after_array_wildcard(self):
        self.model = Model()
        self.model.load([{"key": "v1"}, {"key": "v2"}])
        _, _, options = autocomplete("$[*][", self.model.query)
        self.assertEqual(["['key']"], options)

    # filters
    def test_open_filter(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$[?(", self.model.query)
        self.assertEqual(["@.key"], options)

    def test_open_filter_with_only_question_mark(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$[?", self.model.query)
        self.assertEqual(["("], options)

    def test_nested_list_with_single_dot(self):
        self.model = Model()
        self.model.load({"key": ["item1", "item2"]})
        is_partial_complete, _, options = autocomplete("$.key.", self.model.query)
        self.assertEqual(["[*]", "[0]", "[1]"], options)
        self.assertFalse(is_partial_complete)

    def test_dotted_open_filter(self):
        self.model = Model()
        self.model.load({"key": "value"})
        _, _, options = autocomplete("$.[?(", self.model.query)
        self.assertEqual(["@.key"], options)

    def test_incomplete_filter_after_array_wildcard(self):
        self.model = Model()
        self.model.load([{"key": "v1"}, {"key": "v2"}])
        _, _, options = autocomplete("$[*][?(", self.model.query)
        self.assertEqual(["@.key"], options)

    # union
    def test_incomplete_union_comma(self):
        self.model = Model()
        self.model.load({"k1": "v1", "k2": "v2"})
        _, _, options = autocomplete("$.['k1',", self.model.query)
        self.assertEqual(["'k2'"], options)

    def test_incomplete_union_second_key(self):
        self.model = Model()
        self.model.load({"k1": "v1", "k2": "v2"})
        _, _, options = autocomplete("$.['k1','", self.model.query)
        self.assertEqual(["'k2'"], options)

    def test_incomplete_union_after_array_wildcard(self):
        self.model = Model()
        self.model.load([{"k1": "v1.0", "k2": "v2.0"}, {"k1": "v1.1", "k2": "v2.1"}])
        _, _, options = autocomplete("$[*]['k1','", self.model.query)
        self.assertEqual(["'k2'"], options)

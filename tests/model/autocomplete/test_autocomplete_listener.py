import unittest

from pyfx import Controller
from pyfx.model import Model
from pyfx.model.autocomplete.autocomplete_listener import autocomplete


class AutoCompleteListenerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(Controller())

    def test_empty_string(self):
        options = autocomplete("", self.model.query)
        self.assertEqual(frozenset(["$"]), options)

    def test_single_dot(self):
        self.model.load_from_variable({
            "key": "value"
        })
        options = autocomplete("$.", self.model.query)
        self.assertEqual(frozenset(["*", "key"]), options)

    def test_double_dot(self):
        self.model.load_from_variable({
            "key": "value"
        })
        options = autocomplete("$..", self.model.query)
        self.assertEqual(frozenset([]), options)

    def test_invalid_dots(self):
        # invalid case
        options = autocomplete("$...", self.model.query)
        self.assertEqual(frozenset([]), options)

    def test_dot_incomplete_field(self):
        self.model.load_from_variable({
            "key": "value"
        })
        options = autocomplete("$.k", self.model.query)
        self.assertEqual(frozenset(["key"]), options)

    def test_open_bracket(self):
        self.model.load_from_variable({
            "key": "value"
        })
        options = autocomplete("$[", self.model.query)
        self.assertEqual(frozenset(["[*]", "['key']"]), options)

    def test_dotted_open_bracket(self):
        self.model.load_from_variable({
            "key": "value"
        })
        options = autocomplete("$.[", self.model.query)
        self.assertEqual(frozenset(["[*]", "['key']"]), options)

    def test_incomplete_open_bracket(self):
        self.model.load_from_variable({
            "key": "value"
        })
        options = autocomplete("$.[a", self.model.query)
        self.assertEqual(frozenset([]), options)

    def test_dotted_open_filter(self):
        self.model.load_from_variable({
            "key": "value"
        })
        options = autocomplete("$.[?(", self.model.query)
        self.assertEqual(frozenset(["@.key"]), options)

    def test_invalid_dotted_open_bracket(self):
        options = autocomplete("$...[", self.model.query)
        self.assertEqual(frozenset([]), options)

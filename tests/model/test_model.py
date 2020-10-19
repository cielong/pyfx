import unittest
from unittest.mock import Mock

from pyfx.model.model import Model


class ModelTest(unittest.TestCase):

    controller = Mock()

    def test_single_result_query(self):
        """
        Test py:function:`pyfx.model.model.Model#query(text)`
        with single returned result.
        """
        data = {
            "test": 50
        }

        model = Model(ModelTest.controller)
        model.load_from_variable(data)

        result = model.query("$.test")

        self.assertEqual(50, result)

    def test_multi_result_query(self):
        """
        Test py:function:`pyfx.model.model.Model#query(text)`
        with multiple returned result.
        """
        data = {
            "test": [
                1,
                2,
                3
            ]
        }

        model = Model(ModelTest.controller)
        model.load_from_variable(data)

        result = model.query("$.test[*]")

        self.assertEqual([1, 2, 3], result)

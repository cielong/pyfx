import unittest

from pyfx.model.model import Model


class ModelTest(unittest.TestCase):
    def test_single_result_query(self):
        """
        Test py:function:`pyfx.model.model.Model#query(text)`
        with single returned result.
        """
        data = {
            "test": 50
        }

        model = Model()
        model.load(data=data)

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

        model = Model()
        model.load(data=data)

        result = model.query("$.test[*]")

        self.assertEqual([1, 2, 3], result)

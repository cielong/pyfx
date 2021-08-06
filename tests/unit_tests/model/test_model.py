import unittest

from pyfx.model import DataSourceType
from pyfx.model.model import Model
from pyfx.service.dispatcher import Dispatcher


class ModelTest(unittest.TestCase):
    def test_single_result_query(self):
        """
        Test py:function:`pyfx.model.model.Model#query(text)`
        with single returned result.
        """
        data = {
            "test": 50
        }

        model = Model(Dispatcher())
        model.load(DataSourceType.VARIABLE, data)

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

        model = Model(Dispatcher())
        model.load(DataSourceType.VARIABLE, data)

        result = model.query("$.test[*]")

        self.assertEqual([1, 2, 3], result)

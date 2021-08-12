import unittest

from pyfx.service.dispatcher import Dispatcher


def add(a, b):
    """
    Fake dispatcher method to test invoke.
    """
    return a + b


class DispatcherTest(unittest.TestCase):
    def setUp(self):
        self._dispatcher = Dispatcher()

    def test_invoke(self):
        self._dispatcher.register("add", add)

        result = self._dispatcher.invoke("add", 1, 2)
        self.assertEqual(3, result)

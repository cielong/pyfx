import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

import asynctest

from pyfx.service.client import Client
from pyfx.service.dispatcher import Dispatcher


def add(a, b):
    """
    Fake dispatcher method to test invoke.
    """
    return a + b


class ClientTest(asynctest.TestCase):
    _executor = None

    @classmethod
    def setUpClass(cls):
        cls._executor = ThreadPoolExecutor()

    def setUp(self):
        self._dispatcher = Dispatcher()
        self._my_loop = asyncio.new_event_loop()

    def tearDown(self):
        self._my_loop.close()

    @classmethod
    def tearDownClass(cls):
        cls._executor.shutdown()

    def test_invoke(self):
        self._dispatcher.register("add", add)
        client = Client(self._dispatcher, self.__class__._executor)

        result = client.invoke("add", 1, 2)
        self.assertEqual(3, result)

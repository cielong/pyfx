import asyncio
import unittest
from concurrent.futures.thread import ThreadPoolExecutor

from pyfx.service.client import Client
from pyfx.service.dispatcher import Dispatcher


class ClientTest(unittest.TestCase):
    _executor = None

    @classmethod
    def setUpClass(cls):
        cls._executor = ThreadPoolExecutor()

    def setUp(self):
        self._my_loop = asyncio.new_event_loop()
        self._dispatcher = Dispatcher()

    def tearDown(self):
        self._my_loop.close()

    @classmethod
    def tearDownClass(cls):
        cls._executor.shutdown()

    def test_invoke(self):
        self._dispatcher.register("add", lambda x, y: x + y)
        client = Client(self._dispatcher, self.__class__._executor)

        result = client.invoke("add", 1, 2)
        self.assertEqual(3, result)

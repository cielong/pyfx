import asyncio

import asynctest

from pyfx.service.client import Client
from pyfx.service.dispatcher import Dispatcher


def add(a, b):
    """
    Fake dispatcher method to test invoke.
    """
    return a + b


class ClientTest(asynctest.TestCase):
    def setUp(self):
        self._dispatcher = Dispatcher()
        self._my_loop = asyncio.new_event_loop()

    def tearDown(self):
        self._my_loop.close()

    def test_invoke(self):
        self._dispatcher.register("add", add)
        client = Client(self._dispatcher)

        result = self._my_loop.run_until_complete(client.invoke("add", 1, 2))
        self.assertEqual(3, result)

import asyncio


class Client:
    def __init__(self, dispatcher, executor):
        self._dispatcher = dispatcher
        self._executor = executor

    def invoke(self, path, *args):
        return asyncio.get_event_loop().run_until_complete(
            self._invoke(path, *args))

    def invoke_with_timeout(self, timeout, path, *args):
        return asyncio.get_event_loop().run_until_complete(
            asyncio.wait_for(self._invoke(path, *args), timeout=timeout))

    async def _invoke(self, path, *args):
        return await asyncio.get_event_loop().run_in_executor(
            self._executor, self._dispatcher.invoke, path, *args)

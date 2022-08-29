from collections import defaultdict

from loguru import logger


class ViewMediator:
    """
    A centralized mediator to handle signal.
    """

    def __init__(self):
        # signal -> [(handler, callback),...]
        self._handlers = defaultdict(list)

    def register(self, handler, signal, callback):
        self._handlers[signal].append((handler, callback))

    def notify(self, source, signal, *args, **kwargs):
        """
        Broadcast signals to all the listeners registered for the signal and
        collect result.
        """
        if signal not in self._handlers:
            logger.warning(
                f"Received unknown signal '{signal}' from source '{source}'.")
            return
        results = []
        for handler, callback in self._handlers[signal]:
            results.append((handler, callback(*args, **kwargs)))
        return results

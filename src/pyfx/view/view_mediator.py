from collections import defaultdict

from loguru import logger


class ViewMediator:
    """A centralized mediator to handle signal.

    This mediator is different from `urwid.signals` that it also supports 1-1
    signal.
    """

    def __init__(self):
        # signal -> handler -> callback
        self._handlers = defaultdict(dict)

    def register(self, handler, signal, callback):
        self._handlers[signal][handler] = callback

    def notify(self, source, signal, destination, *args, **kwargs):
        """Sends signal to the intended listener registered for the signal and
        wait on the result.
        """
        if signal not in self._handlers.keys():
            logger.warning(
                f"Received unknown signal '{signal}' from source '{source}'.")
            return None

        if destination not in self._handlers[signal]:
            logger.warning(
                f"Received signal '{signal}' from source '{source}', but "
                f"{destination} does not register handler for the signal.")
            return None

        return self._handlers[signal][destination](*args, **kwargs)

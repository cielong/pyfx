class DispatcherError(Exception):
    pass


class Dispatcher:
    def __init__(self):
        self._paths = {}

    def register(self, path, callback):
        if path in self._paths:
            raise ValueError(
                f"Attempted to register duplicate path {path} in dispatcher."
            )
        self._paths[path] = callback

    def invoke(self, path, *args, **kwargs):
        if path not in self._paths:
            raise DispatcherError(
                f"Path {path} is undefined."
            )
        return self._paths[path](*args, **kwargs)

"""A not-selectable text widget wrapper to show warning messages."""
import threading
import time

import urwid


class WarningBar(urwid.WidgetWrap):
    def __init__(self):
        self._lock = threading.Lock()
        self._update_time = time.time()
        # Starts with empty warning message.
        super().__init__(urwid.Text(""))

    def message(self):
        """Test-use method to get the current warning message"""
        self._lock.acquire()
        try:
            return self._w.text
        finally:
            self._lock.release()

    def update(self, message):
        """Updates the message in the warning bar."""
        self._lock.acquire()
        try:
            self._update_time = time.time()
            self._w.set_text(message)
        finally:
            self._lock.release()

    def clear(self, triggered_action):
        """Clear the warning message in the warding bar."""
        self._lock.acquire()
        try:
            if triggered_action == "keypress":
                self._w.set_text("")
            elif triggered_action == "timeout" and \
                    self._update_time <= time.time() - 10:
                self._w.set_text("")
        finally:
            self._lock.release()

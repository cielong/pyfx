#! /usr/bin/env python3

from typing import NoReturn

import urwid

from pyfx.model.Model import Model
from pyfx.view.view import View


class Controller:
    """ controller """

    def __init__(self, config_file: str = None):
        self._config = config_file
        self._screen = urwid.raw_display.Screen()
        self._view = View(self)
        self._model = Model(self)
        self._loop = None

    def main(self, file_name: str) -> NoReturn:
        self._view.set_data(self._model.load_data(file_name))
        self._loop = urwid.MainLoop(
            self._view.main_window(), self._view.palette,
            screen=self._screen, unhandled_input=self._view.unhandled_input
        )
        self._loop.run()

    def exit(self, exception: Exception):
        raise urwid.ExitMainLoop(exception)

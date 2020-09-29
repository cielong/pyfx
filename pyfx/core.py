#! /usr/bin/env python3
from typing import NoReturn

import urwid

from pyfx.model.model import Model
from pyfx.view.view import View


class Controller:
    """ controller """

    def __init__(self, config_file: str = None):
        self._config = config_file
        self._view = View(self)
        self._model = Model(self)

    def main(self, file_name: str) -> NoReturn:
        self._view.run(self._model.load_data(file_name))

    def autocomplete(self, widget, text):
        options = self._model.autocomplete(text)
        self._view.pop_up_autocomplete_options(options)

    def exit(self, exception):
        self._view.exit(exception)

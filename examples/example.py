#! /usr/bin/env python3

"""This example shows how to load a JSON file and run a `pyfx` TUI. """

import pathlib
from pyfx import Controller

here = pathlib.Path(__file__).parent.parent.resolve()

if __name__ == "__main__":
    Controller().run_with_file(here / "data/data.json")

#! /usr/bin/env python3

"""This example shows how to load a JSON file and run a `pyfx` TUI. """

import pathlib
from pyfx import PyfxApp
from pyfx.model import DataSourceType

here = pathlib.Path(__file__).parent.parent.resolve()

if __name__ == "__main__":
    PyfxApp().run(DataSourceType.FILE, here / "data/data.json")

#! /usr/bin/env python3
#
# This is an example of loading json file
import pathlib
from pyfx import Controller

here = pathlib.Path(__file__).parent.parent.resolve()

if __name__ == "__main__":
    Controller().main(here / "data/data.json")

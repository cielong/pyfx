#! /usr/bin/env python3

"""
This example shows how to run the `pyfx` TUI with in-memory Python variable.
"""

import json
import pathlib
from pyfx import PyfxApp

# Load data from file '../data/data.json'
parent_dir = pathlib.Path(__file__).parent.parent.resolve()
data = json.loads(parent_dir / "data" / "data.json")

# start Pyfx
PyfxApp(data=data).run()

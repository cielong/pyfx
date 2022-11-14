#! /usr/bin/env python3

"""
This example shows how to run the `pyfx` TUI with in-memory Python variable.
"""

from pyfx import PyfxApp

data = {
    "_id": "5fa3b186b8514adb028cb125",
    "name": "Luella Cervantes",
    "age": 40,
    "gender": "woman",
    "phone": [
        "+1 (802) 435-3462"
    ],
    "address": "554 King Street, Tryon, Idaho, 5640"
}

# start Pyfx
PyfxApp(data=data).run()

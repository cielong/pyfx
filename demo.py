#! /usr/bin/env python3
#
# This is an example of loading json file

import json
from pyfx.Browser import Browser

if __name__ == "__main__":
    parent = {"name": "example", "children":[]}
    with open("data/example.json", 'r') as f:
        data = json.load(f)
        Browser(data).main()

#! /usr/bin/env python3


import json
from pyfx.Browser import Browser

def convert(parent, data):
    for k, v in data.items():
        if isinstance(v, dict):
            child = {
                "name": f"{k}",
                "children": []
            }
            parent["children"].append(convert(child, v))
        else:
            child = {
                "name": f"{k}: {v}"
            }
            parent["children"].append(child)
    return parent

if __name__ == "__main__":
    parent = {"name": "example", "children":[]}
    with open("data/example.json", 'r') as f:
        data = json.load(f)
        parent = convert(parent, data)
        Browser(parent).main()

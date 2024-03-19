#!/usr/bin/python3
"""Define a function that create a python object from JSON file."""


import json


def load_from_json_file(filename):
    """Create an object from JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return (json.loads(f.read()))

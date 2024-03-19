#!/usr/bin/python3
"""Define a function that deserialize JSON string to python object."""


import json


def from_json_string(my_str):
    """Convert JSON string to python object.
       Arg:
          my_str (str): JSON string.
       Return:
          Deserialized JSON string result
    """
    return (json.loads(my_str))

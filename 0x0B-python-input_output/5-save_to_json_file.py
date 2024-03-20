#!/usr/bin/python3
"""Define a function that write an object to JSON file."""


import json


def save_to_json_file(my_obj, filename):
    """Serialize object to JSON file and save it into JSON file.
       Args:
           my_obj (object): The object
           filename (file): The file
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

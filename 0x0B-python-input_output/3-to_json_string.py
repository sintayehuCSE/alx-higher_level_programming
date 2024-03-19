#!/usr/bin/python3
"""Define a function that convert python data structure to JSON string."""


import json


def to_json_string(my_obj):
    """Serialize python object to JSON string.
       Args:
           my_obj (object): The object
       Return:
           The JSON string equivalent of the object
    """
    return (json.dumps(my_obj))

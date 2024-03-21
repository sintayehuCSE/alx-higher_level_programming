#!/usr/bin/python3
"""Define a function that return a dictionary description of a simple
   data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returun the objects dictionary."""
    return (obj.__dict__)

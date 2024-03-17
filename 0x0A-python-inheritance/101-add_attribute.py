#!/usr/bin/python3
"""Define a function that add new_attribute to an object
   if possible.
"""


def add_attribute(obj, name, value):
    if hasattr(obj, "__dict__"):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")

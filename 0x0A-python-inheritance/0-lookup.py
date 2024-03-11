#!/usr/bin/python3
"""Define one function that will lookup a dictionary of
   Python objects/instances.
"""


def lookup(obj):
    """Lookup the dictionary of an object.
    Args:
        obj (python object): The object.
    Return:
          The List form of object dictionary
    """
    return (list(dir(obj)))

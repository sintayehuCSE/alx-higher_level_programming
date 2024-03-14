#!/usr/bin/python3
"""Define a function that check if an instance is
   the exact instanc of a class.
"""


def is_same_class(obj, a_class):
    """Check if an object is an exact instance of a class.
    Args:
        obj (object): The object
        a_class (class): The class
    Return:
        True: If object is exact instance of a_class
        False: If obj is not exact instance of a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False

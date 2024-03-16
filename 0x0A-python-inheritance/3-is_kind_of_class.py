#!/usr/bin/python3
"""Define a function that determine the class to which an
   Instance belongs.
"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of a class or its parents.
    Args:
        obj (object): The object
        a_class (class): The class
    Return:
        True: If obj is instance of a_class
        False: If obj is not instance of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
"""Has one function that check if class of an object is a
   subclass of anouther class.
"""


def inherits_from(obj, a_class):
    """Checks if obj 'obj' class is a subclass of 'a_class'.
    Args:
        obj (object): The object
        a_class (class): The parent class (supposedly)
    Return:
        True: If 'obj' class is subclass of 'a_class'.
        False: If 'obj' class id not subclass of 'a_class'.
    """
    if issubclass(type(obj), a_class):
        if type(obj) is a_class:
            return False
        return True
    else:
        return False

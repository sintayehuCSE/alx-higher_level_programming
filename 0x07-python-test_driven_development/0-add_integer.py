#!/usr/bin/python3
"""This module defines a function add_integer(a, b=98).
   The function is used to add together two integer variables.

   The two arguments need to be an exact integer.
"""


def add_integer(a, b=98):
    """Initiates the addition of two integers.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    """
    if not isinstance(a, (int, float)) or type(a) is None:
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)) or type(b) is None:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

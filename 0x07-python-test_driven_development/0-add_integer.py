#!/usr/bin/python3
"""This module defines a function add_integer(a, b=98).
   The function is used to add together two integer variables.

   The two arguments need to be an exact integer."""


def add_integer(a, b=98):
    """Initiates the addition of two integers.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)

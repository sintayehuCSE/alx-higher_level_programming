#!/usr/bin/python3
"""Defines a function that print a SQUARE with '#' character representation."""


def print_square(size):
    """Draw a SQUARE with '#' character.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not int type.
        ValueError: If size is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            [print("#", end="") for j in range(size)]
            print()

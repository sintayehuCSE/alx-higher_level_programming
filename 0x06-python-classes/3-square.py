#!/usr/bin/python3
"""Defines a class named Square."""


class Square:
    """This is the square class"""
    def __init__(self, size=0):
        """Initialize the classe's object.
        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the size of the square."""
        return (self.__size ** 2)

#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Represent the class Square."""
    def __init__(self, size=0):
        """Initialize the class instance attribute.
        Args:
            size (int): The size of the square
        """
        self.size = size
    @property
    def size(self):
        """Get the value of object attribute."""
        return (self.__size)
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

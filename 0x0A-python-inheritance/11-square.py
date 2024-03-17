#!/usr/bin/python3
"""Define the Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class."""
    def __init__(self, size):
        """Initialize the Square."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """The area of a square."""
        return (self.__size * self.__size)

    def __str__(self):
        """The string representation of Square object."""
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))

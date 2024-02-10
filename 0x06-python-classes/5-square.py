#!/usr/bin/python3
"""Defines a class named Square."""


class Square:
    """The Square class."""
    def __init__(self, size=0):
        """Initialize the size of the Square class.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Draw the square with character #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end=" ")
            print()
        if (self.__size == 0):
            print()

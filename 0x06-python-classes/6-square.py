#!/usr/bin/python3
"""Defines a class named Square."""


class Square():
    """The Square class."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class attributes for its instance.
        Args:
            size (int): The size of the square
            position (tuple): The position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/Return the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Get the area of the current square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Draw the square with # character."""
        if self.__size == 0:
            print()
        [print() for i in range(self.__position[1]) if self.__size != 0]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            for j in range(self.__size):
                print("#", end="")
            print()

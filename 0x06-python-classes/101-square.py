#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Define a Square class."""
    def __init__(self, size=0, position=(0,0)):
        """Initialize the Square object.
        Args:
            size (int): The size of the Square object.
            position (int, int): The position of the square.
        """
        self.__size = size
        self.__position = position
        self.__str = 0

    @property
    def size(self):
        """Get/Return the size of Square object."""
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
        """Get/Return the position of the Square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not all(isinstance(value, tuple) and isinstance(value[0], int)
               and isinstance(value[1], int) and value[0] >= 0 and
               value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """Get/Return the area of the current square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print/draw the square with the character #."""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for j in range(self.__size)]
                if (self.__str == 0):
                    print()
                elif (self.__str) and (i != (self.__size - 1)):
                    print()
    def __str__(self):
        """The string representation of square object."""
        self.__str = 1
        self.my_print()
        return ("")

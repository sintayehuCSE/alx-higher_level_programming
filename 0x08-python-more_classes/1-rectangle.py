#!/usr/bin/python3
"""Define one class."""


class Rectangle:
    """Define the Rectangle class."""
    def __init__(self, width, height):
        """Initialize the Rectangle instance.
           Args:
               width (int): Width of the rectangle.
               height (int): Height of the rectangle.
           Raises:
               TypeError: If either width or height is not int object.
               ValueError: If either width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

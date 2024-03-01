#!/usr/bin/python3
"""Define one class."""


class Rectangle:
    """Define the rectangle class."""
    def __init__(self, width=0, height=0):
        """Initialize the instance of a rectangle.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        Raises:
            TypeError: If width or height is not int object.
            ValueError: If width or height is less than zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property for width of the rectangle."""
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
        """Property for the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter of a rectangle."""
        if not self.width or not self.height:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """The string representation of rectangle object."""
        if self.width and self.height:
            for i in range(self.height):
                [print("#", end="") for j in range(self.width)]
                if i != (self.height - 1):
                    print()
        else:
            return ("")

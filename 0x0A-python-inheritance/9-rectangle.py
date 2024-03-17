#!/usr/bin/python3
"""Define the Rectangle class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implement the Rectangle class."""
    def __init__(self, width, height):
        """Initialize the instance of Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Get the area of a Rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """The unofficial printable string representation
           of Rectangle object.
        """
        return ('[Rectangle] ' + str(self.__width) + '/' + str(self.__height))

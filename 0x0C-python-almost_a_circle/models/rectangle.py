#!/usr/bin/python3
"""Define a rectangle class."""


from models.base import Base


class Recatangle(Base):
    """The rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the instance of a rectangle.
        """
        super(Base, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of a rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Gets the height of a rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Get the value of 'x' coordinate."""
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Gets the value of a 'y' coordinate."""
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value

#!/usr/bin/python3
"""Defines the special type of rectangle - Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define the Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance of a Square.
           Args:
               size (int): The size of the square.
               x (int): The 'x' coordinate of the square instance.
               y (int): The 'y' coordinate of the square instance.
               id (int): The id of the Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return nice printable string representation of the string object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

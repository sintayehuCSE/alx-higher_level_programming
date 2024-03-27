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

    def update(self, *args, **kwargs):
        """Update the attribute of Square instance.
           Args:
               args (tuple): Tuble of non=keyworded argument list
               kwargs (dict): Dictionary of key-worded argument list
        """
        if args:
            for i in range(len(args)):
                if i == 4:
                    break
                elif i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if kwargs:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    elif key == "size":
                        self.size = kwargs[key]
                    elif key == "x":
                        self.x = kwargs[key]
                    elif key == "y":
                        self.y = kwargs[key]

    def __str__(self):
        """Return nice printable string representation of the string object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

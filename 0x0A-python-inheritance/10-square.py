#!/usr/bin/python3
"""Define the Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class."""
    def __init__(self, size):
        """Initialize the Square."""
        Rectangle.__init__(self, size, size)

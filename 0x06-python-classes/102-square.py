#!/usr/bin/python3
"""Container for a class Square.

   This class also defines the 'Rich comparison methods for
   its instances'
"""


class Square:
    """Define the Square class."""
    def __init__(self, size=0):
        """Initialize the size of the new instance of Square.
        Args:
            size (int): The size of the new Squaree instance.
        """
        self.__size = size

    @property
    def size(self):
        """Get/Return the size of the Square instance."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Get/Return the area of the Square instance."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Define the == comparison operator for class Square instance.
        Args:
           self (<class 'Square'>): The first operand
           other (<class 'Square'>): The second operand
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """Define the != comparison operator for class Square instance."""
        return (self.area() != other.area())

    def __gt__(self, other):
        """Define the > comparison operator for class Square instance."""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Define then >= comparison operator for class Square instance."""
        return (self.area() >= other.area())

    def __lt__(self, other):
        """Define the < comparison operator for class Square instance."""
        return (self.area() < other.area())

    def __le__(self, other):
        """Define the <= comparison operator for class Square instance."""
        return (self.area() <= other.area())

#!/usr/bin/python3
"""Conversion of CPython bytecode to class."""
import math


class MagicClass:
    """Magic class to convert bytecode."""
    def __init__(self, radius=0):
        """Initialize the radius.
        Args:
            radius (int, float): radius of the class
        """
        self.__radius = 0

    @property
    def radius(self):
        """Get the value of the class radius."""
        return (self.__radius)

    @radius.setter
    def radius(self, value):
        if not all(isinstance(value, (int, float))):
            raise TypeError("radius must be a number")
        else:
            self.__radius = value

    def area(self):
        """Area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)

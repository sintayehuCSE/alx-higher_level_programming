#!/usr/bin/python3
"""Conversion of CPython bytecode to class."""
import math


class MagicClass:
    """Magic class to convert bytecode."""
    def __init__(self, radius=0):
        self.__radius = 0

    @property
    def radius(self):
        return (self.__radius)

    @radius.setter
    def radius(self, value):
        if not all(isinstance(value, (int, float))):
            raise TypeError("radius must be a number")
        else:
            self.__radius = value

    def area(self):
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)

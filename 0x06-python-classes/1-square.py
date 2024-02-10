#!/usr/bin/python3
"""A module/file containing defining a class that will
intialize a private attribute of an object
"""


class Square:
    """Defines a private instance attribute"""
    def __init__(self, size):
        """Initialize the size attribute of an instance"""
        self.__size = size

#!/usr/bin/python3
"""Defines a base class for this project."""


class Base:
    """The base class of this project.

       This class will be the base of all other classes in this project.
       The goal of it is to manage id attribute in all future classes and
       to avoid duplicating the same code (by extension, same bugs).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

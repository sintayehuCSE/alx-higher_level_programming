#!/usr/bin/python3
"""Define a custom List class."""


class MyList(list):
    """The subclass of list class"""
    def print_sorted(self):
        print(sorted(self))

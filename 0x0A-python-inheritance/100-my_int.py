#!/usr/bin/python3
"""Define a custom integer class."""


class MyInt(int):
    """The custom integer class."""
    def __eq__(self, other):
        """Compare self with other"""
        return (not (int.__eq__(self, other)))

    def __ne__(self, other):
        """The not equal comparison."""
        return (not (int.__ne__(self, other)))

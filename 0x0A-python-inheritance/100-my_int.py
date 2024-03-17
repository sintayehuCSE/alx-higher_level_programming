#!/usr/bin/python3
"""Define a custom integer class."""


class MyInt(int):
    """The custom integer class."""
    def __eq__(self, other):
        """Compare self with other"""
        if self == other:
            return False
        return True

    def __ne__(self, other):
        """The not equal comparison."""
        if self == other:
            return True
        else:
            return False

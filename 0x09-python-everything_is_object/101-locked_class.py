#!/usr/bin/python3
"""Define a Low memory cost class."""


class LockedClass:
    """Defines a LockeClass that limit an attribute of its instance to one."""
    __slots__ = ["first_name"]

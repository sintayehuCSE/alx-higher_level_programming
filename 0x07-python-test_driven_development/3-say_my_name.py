#!/usr/bin/python3
"""Deines a say_my_name function that will print a given name."""


def say_my_name(first_name, last_name=""):
    """Prints a full name, <first name> and <last name>.

    Args:
        first_name (str): The first name.
        last_name (str): The sur name.

    Raises:
        TypeError: If any of the name is not string.
        TypeError: if any of the character in each name unit is not alphabet.
        ValueError: if first name is empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif not first_name:
        raise ValueError("first_name cannot be empty")
    for char in first_name:
        c = ord(char)
        if c < 65 or (c > 90 and c < 97) or c > 122:
            raise ValueError("first_name should be made of alphabets")
    for char in last_name:
        c = ord(char)
        if c < 65 or (c > 90 and c < 97) or c > 122:
            raise ValueError("last_name should be made of alphabets")
    print("My name is", first_name, last_name)

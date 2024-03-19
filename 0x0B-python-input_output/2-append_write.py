#!/usr/bin/python3
"""Define a function that will append a text to a file."""


def append_write(filename="", text=""):
    """Append a text ot end of a file.
       Args:
           filename (str): A file
           text (str): The text
       Return:
            The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))

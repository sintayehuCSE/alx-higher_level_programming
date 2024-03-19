#!/usr/bin/python3
"""Define a function that write to a file."""


def write_file(filename="", text=""):
    """Writes a text to the specified file.
       Args:
           filename (str): The file name.
           text (str): The text to write into a file.
       Return:
           The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))

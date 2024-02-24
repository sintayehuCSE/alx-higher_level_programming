#!/usr/bin/python3
"""Defines a function that will parse a string to collect its substring
   based on occurence of delimiter (., :, ?). And print out the substring.
"""


def text_indentation(text):
    """Parse a string to print a substring of it.

    The substring are denoted by occurence of '.', '?', or ':' characters.
    Args:
        text (str): The substring to parse through.
    Raises:
        TypeError: If text is not string type.
        TypeError: If text is not provided.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    elif not text:
        raise ValueError("text should not be empty")
    size = 0
    dlm = ".?: "
    for char in text:
        if char not in dlm:
            print(char, end="")
        else:
            if (char in ' ' and (size + 1) < len(text)):
                if (text[size + 1] not in dlm and text[size - 1] not in dlm):
                    print(char, end="")
            elif char in ":?.":
                print(char)
                print()
        size += 1

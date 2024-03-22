#!/usr/bin/python3
"""Define a function that search for substring on a file line and
   Enter a new line in for each occurence of the substring.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a new line text in to a file."""
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readlines()
    with open(filename, "w", encoding="utf-8") as f2:
        for item in line:
            if search_string in item:
                f2.write(item + new_string)
            else:
                f2.write(item)

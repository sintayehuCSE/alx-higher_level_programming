#!/usr/bin/python3
"""This module define one function read_file(...) that reads a text."""


def read_file(filename=""):
    """Opens a file for reading and print it to stdout.
       Args:
           filename (str): The filename/its absolute path
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

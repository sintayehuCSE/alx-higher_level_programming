#!/usr/bin/python3
def magic_string():
    magic_string.i = getattr(magic_string, 'i', 0) + 1
    if magic_string.i > 1:
        print("BestSchool, " * (magic_string.i - 1), end="")
        return "BestSchool"
    else:
        return "BestSchool"

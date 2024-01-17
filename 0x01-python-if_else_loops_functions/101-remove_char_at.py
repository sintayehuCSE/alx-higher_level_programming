#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        print("{}".format(str), end='')
        return ''
    for char in str:
        if char != str[n] and n >= 0:
            print("{}".format(char), end='')
    return ''

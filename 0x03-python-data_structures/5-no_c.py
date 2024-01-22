#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    if my_string:
        for i in range(len(my_string)):
            if my_string[i] != 'C' and my_string[i] != 'c':
                new_str = new_str + my_string[i]
    return new_str

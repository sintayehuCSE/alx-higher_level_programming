#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = -1
    if my_list:
        while (i >= -(len(my_list))):
            print("{:d}".format(my_list[i]))
            i = i - 1

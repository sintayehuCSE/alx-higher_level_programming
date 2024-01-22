#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        if my_list[0] >= 0:
            max_item = 0
        else:
            max_item = my_list[0]
        for item in my_list:
            if item > max_item:
                max_item = item
    else:
        return "None"
    return max_item

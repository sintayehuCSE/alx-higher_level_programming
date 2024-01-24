#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for unq in my_list:
        status = True
        if len(new_list) == 0:
            new_list.append(unq)
            continue
        for i in range(len(new_list)):
            if unq == new_list[i]:
                status = False
        if status:
            new_list.append(unq)
    for i in new_list:
        result += i
    return result

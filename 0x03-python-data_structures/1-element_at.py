#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)

    if idx < 0:
        return
    elif idx >= list_len:
        return
    else:
        return my_list[idx]

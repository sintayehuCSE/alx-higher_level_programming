#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)
    if len_tuple_a >= 2 and len_tuple_b >= 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
    elif len_tuple_a < 2 or len_tuple_b < 2:
        if len_tuple_a < 2 and len_tuple_b >= 2:
            if len_tuple_a == 0:
                a = tuple_b[0]
                b = tuple_b[1]
            else:
                a = tuple_a[0] + tuple_b[0]
                b = tuple_b[1]
        elif len_tuple_a >= 2 and len_tuple_b < 2:
            if len_tuple_b == 0:
                a = tuple_a[0]
                b = tuple_a[1]
            else:
                a = tuple_a[0] + tuple_b[0]
                b = tuple_a[1]
        else:
            if len_tuple_a == 0 and len_tuple_b == 1:
                a = tuple_b[0]
            elif len_tuple_a == 1 and len_tuple_b == 0:
                a = tuple_a[0]
            elif len_tuple_a == 1 and len_tuple_b == 1:
                a = tuple_a[0] + tuple_b[0]
    new_tuple = (a, b)
    return new_tuple

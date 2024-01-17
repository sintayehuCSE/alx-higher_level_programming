#!/usr/bin/python3
def pow(a, b):
    result = a
    expo = False
    if b < 0:
        b *= -1
        expo = True
    for i in range(b - 1):
        result *= a
    if expo:
        return 1 / result
    if b == 0:
        return 1
    return result

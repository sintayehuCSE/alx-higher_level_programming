#!/usr/bin/python3
"""This module define a function that construct a pascal's triangle."""


def pascal_triangle(n):
    """Construct the pascal's triangle."""
    pt = []
    if n <= 0:
        return (pt)
    else:
        item = []
        i = 0
        while (i < n):
            if i == 0:
                item.append(1)
                pt.append(item)
            else:
                prev = pt[i - 1]
                item = []
                item.append(1)
                j = 0
                ln = len(prev)
                while (j < ln):
                    i1 = prev[j]
                    if ((j + 1) < ln):
                        i2 = prev[j + 1]
                    else:
                        i2 = 0
                        i1 = 1
                    item.append(i1 + i2)
                    j += 1
                pt.append(item)
            i = i + 1
    return (pt)

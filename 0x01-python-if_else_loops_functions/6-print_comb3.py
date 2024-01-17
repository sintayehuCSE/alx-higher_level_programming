#!/usr/bin/python3
for num in range(0, 10):
    for i in range(num + 1, 10):
        if (num == 8 and i == 9):
            print("{}{}".format(num, i))
        else:
            print("{}{}, ".format(num, i), end='')

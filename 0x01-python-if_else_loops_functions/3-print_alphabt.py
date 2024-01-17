#!/usr/bin/python3
i = 97
while i < 123:
    if chr(i) != 'q' and chr(i) != 'e':
        print("{:c}".format(i), end="")
    i += 1

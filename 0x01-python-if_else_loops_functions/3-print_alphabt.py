#!/usr/bin/python3
i = 97
while i < 123:
    if chr(i) != 'q' and chr(i) != 'e':
        print(f"{i:c}", end="")
    i += 1

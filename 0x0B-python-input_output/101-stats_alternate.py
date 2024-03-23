#!/usr/bin/python3
"""A script that reads `stdin` line by line and computes metrics"""


import sys


line_content = []
code = [200, 301, 400, 401, 403, 404, 405, 500]
found = []
line_no = 0
file_size = 0
try:
    for line in sys.stdin:
        line_content.append(line)
        line_no += 1
        if line_no == 10:
            for item in line_content:
                file_size += len(item)
                for cd in code:
                    if str(cd) in item:
                        found.append(cd)
            found.sort()
            line_content.clear()
            line_content = []
            line_no = 0
            print("File size: {:d}".format(file_size))
            [print(item, ":") for item in found]
            found.clear()
            found = []
except KeyboardInterrupt as e:
    if line_content:
        for item in line_content:
            file_size += len(item)
            for cd in code:
                if str(cd) in item:
                    found.append(cd)
        found.sort()
        print("File size: {:d}".format(file_size))
        [print(item, ":") for item in found]
    raise e

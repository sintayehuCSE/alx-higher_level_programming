#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum_cmd = 0
    for i in range(len(argv) - 1):
        sum_cmd += int(argv[i + 1])
    print("{}".format(sum_cmd))

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum_cmd = 0
    num = len(argv)
    for i in range(1, num):
        sum_cmd += int(argv[i])
    print("{}".format(sum_cmd))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    strlen = len(sys.argv)
    if strlen == 1:
        print("{} arguments.".format(strlen - 1))
    elif strlen == 2:
        print("{} argument:".format(strlen - 1))
        print("{}: {}".format(strlen - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(strlen - 1))
        for i in range(strlen - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))

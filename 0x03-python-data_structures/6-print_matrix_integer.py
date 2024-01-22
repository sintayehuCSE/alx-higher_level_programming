#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    list_1D = []
    for item in matrix:
        list_1D = item
        for i in range(len(list_1D)):
            print("{:d}".format(list_1D[i]), end='')
            if i != len(list_1D) - 1:
                print(" ", end='')
        print("")

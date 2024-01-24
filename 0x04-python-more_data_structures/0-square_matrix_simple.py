#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda row: [row[i] * row[i]
                     for i in range(len(row))], matrix)))

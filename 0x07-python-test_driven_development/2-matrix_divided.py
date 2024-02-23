#!/usr/bin/python3
"""Defines a matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide each element of 'matrix' by 'div'.

    matrix is only a list of lists of either floatsor integers.

    Each row of the 'matrix' should have an equal length.

    'div' can't be zero.
    Args:
        matrix (lists of list): The matrix of lists of list.
        div (int or float): Divisor for each element of 'matrix'.
    Raises:
        Either TypeError, or ZeroDivisionError based on the condition.
    Return:
        A new matrix populated with division result of each element of 'matrix'
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif not div:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
    matrix_len = len(matrix)
    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    return (list(map(lambda row: [round(col / div, 2) for col in row],
                     matrix)))

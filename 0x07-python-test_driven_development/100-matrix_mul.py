#!/usr/bin/python3
"""Defines a function for multiplying two matrices."""


def maniac(item, itr, row_b=[]):
    """Perform row by col multiplicatio.
       Args:
           item (int/float): The items in each row of first matrix.
           itr (int): Iterations through the second matrix rowise.
           row_b (list): Each row of specific iteration from second matrix.
       Returns:
           The multiplication of item and itr-th element of row_b.
    """
    return (item * row_b[itr])


def matrix_mul(m_a, m_b):
    """Multiplies each element of one matrix by the other.
       Args:
           m_a (list): First matrix
           m_b (list): Second matrix
       Raises:
           TypeError: If the argument type is not a list.
           TypeError: If argumets are not a list of lists.
           ValueError: If either argument are empty.
           TypeErro: If any of list of lists elm are not either int/float.
           TypeError: If each row of either argument are not equaly sized.
           ValueError: If the argument can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        if not row:
            raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if not row:
            raise ValueError("m_b can't be empty")
    for row in m_a:
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(m_a[0]) != len(row):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(m_b[0]) != len(row):
            raise TypeError("each row of m_b must be of the same size")
    #WHEN IS TWO MATRIX CAN'T BE MULTIPLIED?, WHEN COLUMN OF m_a IS NOT EQUAL TO
    #ROW OF m_b.
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    product_matrix = []
    for row_a in m_a:
        lists = []
        elm = 0
        itr = 0
        i = 0
        j = 0
        while (i < len(m_b[0])):
            for item in row_a:
                elm = elm + maniac(item, itr, m_b[j])
                j += 1
            j = 0
            lists.append(elm)
            i += 1
            elm = 0
            itr += 1
        product_matrix.append(lists)
    return (product_matrix)

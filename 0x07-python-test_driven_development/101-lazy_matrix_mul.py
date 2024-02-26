#!/usr/bin/python3
"""Defines a function for multiplying two matrices through use of
   NumPy module.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply the first matrix by the second matrix.
       Args:
           m_a (list): The first matrix.
           m_b (list): The second matrix.
       Return:
           The dot product of the two matrix.
    """
    return (np.matmul(m_a, m_b))

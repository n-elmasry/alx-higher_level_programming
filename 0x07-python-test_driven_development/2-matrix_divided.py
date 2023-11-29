#!/usr/bin/python3
"""
matrix_divide
This module defines a function, add_integer(a, b=98), which adds two numbers.

"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    """
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        row_result = []
        for value in row:
            if not isinstance(value, (int, float)):
                msg = 'matrix must be a matrix '\
                        '(list of lists) of integers/floats'
                raise TypeError(msg)
            else:
                result = round(value / div, 2)
                row_result.append(result)
        new_matrix.append(row_result)
    return new_matrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = num ** 2
            new_row.append(result)
        sq_matrix.append(new_row)
    return sq_matrix

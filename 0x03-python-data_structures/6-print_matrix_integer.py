#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            for value in row[:-1]:
                print("{:d}".format(value), end=" ")
            print("{:d}".format(row[-1]))
        else:
            print()

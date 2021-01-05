#!/usr/bin/python3
# prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    """ Prints a matrix of integers. """
    if matrix != [[]]:
        for row in matrix:
            for x in row[:-1]:
                print("{:d}".format(x), end=" ")
            print("{:d}".format(row[-1]))
    else:
        print("")

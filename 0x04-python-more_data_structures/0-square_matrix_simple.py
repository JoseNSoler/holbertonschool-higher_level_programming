#!/usr/bin/python3
# computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[]):
    cp_matrix = []
    for x in matrix:
        cp_matrix.append(list(map((lambda y: y * y), x)))
    return cp_matrix

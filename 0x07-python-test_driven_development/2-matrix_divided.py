#!/usr/bin/python3
'''Function to divide elements of a matrix '''


def matrix_divided(matrix, div):
    '''
    Returns a new matrix with the all elements of 'matrix' divided 
    by div parameter

    Args:
        matrix: given matrix by the user
        div: number to divide all elements
    '''
    new_arr = []
    x, y, = 0, 0

    if div != None:
        if ((not isinstance(div, float) and 
            not isinstance(div, int))):
            raise TypeError("div must be a number")
        if div == 0: raise ZeroDivisionError("division by zero")
    else: raise TypeError("div must be a number")

    for element in matrix:
        for num in element:
            if ((not isinstance(num, float) and 
                not isinstance(num, int))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            x += 1
        y += 1
        
    if x % y == 0:
        for element in matrix: 
            rowList = []
            for num in element: rowList.append(round(num / div, 2))
            new_arr.append(rowList)
    else: raise TypeError("Each row of the matrix must have the same size")

    return new_arr

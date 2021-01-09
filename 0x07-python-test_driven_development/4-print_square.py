#!/usr/bin/python3
'''Function to add integers '''


def print_square(size):
    '''
    Prints a square made of # with size int give by user

    Args:
        size: int number to use
    '''

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float): 
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    
    for x in range(0, size):
        for y in range(0, size): print("#", end='')
        print()

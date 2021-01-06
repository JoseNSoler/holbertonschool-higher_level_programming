#!/usr/bin/python3
''' Square module '''


class Square:
    '''square class'''
    def __init__(self, size=0):
        '''
        first Init

        Args: int to use for size
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Returns area of the square'''
        return(self.__size * self.__size)
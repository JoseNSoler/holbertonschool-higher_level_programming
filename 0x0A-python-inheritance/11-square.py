#!/usr/bin/python3
'''Module - Square 2'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size):
        '''
        Init for class Square

        Args:
            size (int): User's given size for square
        '''
        if (not super(Rectangle, self).integer_validator("size", size)):
            super(Square, self).__init__(size, size)
            self.__size = size

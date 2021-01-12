#!/usr/bin/python3
'''Module for use of a Rectangle'''


class Rectangle:
    '''Empty rectangle '''
    def __init__(self, width=0, height=0):
        """Initial values -new Rectangle.

        Args:
            width (int): Width rectangle.
            height (int): Height rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter for width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width of rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height of rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns area of rectangle '''
        if self.__width == 0 or self.__height == 0: 
            return 0
        return (self.__width * 2) + (self.__height * 2)

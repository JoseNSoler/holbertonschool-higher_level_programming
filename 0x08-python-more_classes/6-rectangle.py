#!/usr/bin/python3
'''Module for use of a Rectangle'''


class Rectangle:
    '''Empty rectangle '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initial values -new Rectangle.

        Args:
            width (int): Width rectangle.
            height (int): Height rectangle.
        """
        type(self).number_of_instances += 1
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

    def __str__(self):
        '''Returns this rectangle maded by # '''
        x_size = self.__width
        y_size = self.__height

        if x_size == 0 or y_size == 0:
            return ("")
        obj = []
        for a in range(y_size):
            [obj.append('#') for b in range(x_size)]
            if a != y_size - 1:
                obj.append("\n")
        return ("".join(obj))

    def __repr__(self):
        '''string representation of a rectangle '''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Deletes a rectangle and prints a message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

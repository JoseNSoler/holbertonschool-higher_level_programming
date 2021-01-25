#!/usr/bin/python3
'''Module - Rectangle'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''sub-class from BaseGeometry '''
    def __init__(self, width, height):
        '''
        Init for class Rectangle <value>

        Args:
            width: User's given width
            height: User's given height
        '''
        if (not super(Rectangle, self).integer_validator("width", width)):
            self.__width = width
        if (not super(Rectangle, self).integer_validator("height", height)):
            self.__height = height

    def area(self):
        '''Returns area of base'''
        return (self.__height * self.__width)

    def __str__(self):
        '''Predefined string for object Rectangle '''

        pre_str = "[Rectangle] "+str(self.__width)+"/"+str(self.__height)
        return pre_str

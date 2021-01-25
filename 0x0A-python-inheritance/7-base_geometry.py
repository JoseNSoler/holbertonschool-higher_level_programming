#!/usr/bin/python3
'''Module - Empty class for base geometry'''


class BaseGeometry:
    '''Empty class BaseGeometry '''
    def area(self):
        '''Area of base - Temporarily out of service '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validator for <value>

        Args:
            name: User's given name
            value: User's given value (must be value, otherwise 
            rise TypeError and ValueError)
        '''
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

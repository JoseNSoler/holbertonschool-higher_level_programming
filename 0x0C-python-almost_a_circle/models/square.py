#!/usr/bin/python3
'''Module - Square geometry'''

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class - Square object '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializer for Square

        Args:
            size: User's given size -- inherits from rectangle
            x: User's given x position
            y: User's given y position
            id: User's given id int for obj. Rectangle
            (validated through Parent class)
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter for size of square'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size of square'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Rectangle.
        Args:
            *args (ints): New given user's attribute value
                - 1st argument= id attribute
                - 2nd argument= size attribute
                - 3rd argument= x attribute
                - 4th argument= y attribute
            //Second Update:
                **kwargs (dict): key/value pairs of attributes
        """
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.size = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary with values of object Square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''Default print string'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                       self.x, self.y,
                                                       self.size)

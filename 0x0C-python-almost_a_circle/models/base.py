#!/usr/bin/python3
'''Module - base geometry '''


class Base:
    '''Class - Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializer for base

        Args:
            id: User's given id int for obj. Base
            (otherwise, int of __nb__objects will be assigned to id)
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

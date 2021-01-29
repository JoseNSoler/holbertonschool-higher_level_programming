#!/usr/bin/python3
''' Module - Student objectls '''


class Student(object):
    '''Class Student'''

    def __init__(self, first_name, last_name, age):
        '''
        Initializer for class Student

        Args:
            first_name = User's given name
            last_name = User's given last name
            age = User's given age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns a structure data of our Class '''
        x = 0
        if attrs is not None:
            for elem in attrs:
                if (type(elem) == str):
                    x += 1

        if (type(attrs) == list and x == len(attrs)):
            dicto = {}
            for y in attrs:
                if hasattr(self, y):
                    tmp = getattr(self, y)
                    dicto[y] = tmp
            return dicto
        return self.__dict__

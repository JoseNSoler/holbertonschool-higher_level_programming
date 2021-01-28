#!/usr/bin/python3
''' Module - Student object '''


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
    
    def to_json(self):
        '''Returns a structure data of our Class '''
        obj_att = self.__dict__
        return (obj_att)

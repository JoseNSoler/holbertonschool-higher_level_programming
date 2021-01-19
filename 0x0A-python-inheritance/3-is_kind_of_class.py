#!/usr/bin/python3
'''
Module - check if a variable s an instance of, or if the object
is an instance of a class that inherited from
'''


def is_kind_of_class(obj, a_class):
    '''
    Args:
        obj: object to analyze
        a_class(Type): type of data to compare

    Returns:
        True in a coincidence
    '''

    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    return False

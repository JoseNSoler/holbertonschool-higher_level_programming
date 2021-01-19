#!/usr/bin/python3
'''
Module - check if a variable object is an instance
of a class that inherited (directly or indirectly) from
the specified class
'''


def inherits_from(obj, a_class):
    '''
    Args:
        obj: object to analyze
        a_class(Type): type of data to compare

    Returns:
        True in a coincidence
    '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

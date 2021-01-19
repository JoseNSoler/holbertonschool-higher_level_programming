#!/usr/bin/python3
'''Module - check if a variable is same class of a type'''


def is_same_class(obj, a_class):
    '''
    Args:
        obj: object to analyze
        a_class(Type): type of data to compare

    Returns:
        True in a coincidence
    '''

    if type(obj) == a_class:
        return True
    return False

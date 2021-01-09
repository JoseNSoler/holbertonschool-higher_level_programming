#!/usr/bin/python3
'''Module for print name'''


def say_my_name(first_name, last_name=""):
    '''
    Prints: My name is - first name - last name

    Args:
        first_name: first name given by the user
        last_name: last name given by the user
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

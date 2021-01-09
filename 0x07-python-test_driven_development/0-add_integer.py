#!/usr/bin/python3
'''Function to add integers '''


def add_integer(a, b=98):
    '''
    Return a integer of two int or floats converted to int

    Raises:
        TypeError: a or b are different types of expected

    '''

    if ((not isinstance(a, float) and not isinstance(a, int))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

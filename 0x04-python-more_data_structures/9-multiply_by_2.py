#!/usr/bin/python3
#  returns a new dictionary with all values multiplied by 2.


def multiply_by_2(a_dictionary):
    return ({x: a_dictionary[x] * 2 for x in a_dictionary})

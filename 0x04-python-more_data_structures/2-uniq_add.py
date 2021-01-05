#!/usr/bin/python3
# adds all unique integers in a list (only once for each integer)


def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result = result + x
    return (result)

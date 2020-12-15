#!/usr/bin/python3
# finds the biggest integer of a list


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    bigger = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > bigger:
            bigger = my_list[x]

    return (bigger)

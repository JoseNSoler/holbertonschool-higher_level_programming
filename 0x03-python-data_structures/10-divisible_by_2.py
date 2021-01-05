#!/usr/bin/python3
# finds all multiples of 2 in a list


def divisible_by_2(my_list=[]):
    multiples = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)

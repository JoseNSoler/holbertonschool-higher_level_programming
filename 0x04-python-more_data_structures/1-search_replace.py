#!/usr/bin/python3
# replaces all occurrences of an element by another in a new list


def search_replace(my_list, search, replace):
    cop_list = my_list[:]
    for x in range(len(cop_list)):
        if cop_list[x] == search:
            cop_list[x] = replace
    return (cop_list)

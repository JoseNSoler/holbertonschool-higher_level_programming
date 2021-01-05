#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """Print x elememts of a given list.
    Args:
        my_list (list): List to analyze
        x (int): Number of elements to print
    Returns:
        n numbers printed
    """

    val = 0
    for x in range(x):
        try:
            print("{}".format(my_list[x]), end="")
            val += 1
        except IndexError:
            break
    print("")
    return (val)
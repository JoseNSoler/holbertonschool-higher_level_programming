#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    """ Prints the first x elements of a list and only integers.
    Args:
        my_list (list): given list to analize
        x (int): n items to print
    Returns:
        real number of integers printed
    """

    val = 0
    for x in range(x):
        try:
            print("{:d}".format(my_list[x]), end="")
            val += 1
        except (ValueError, TypeError):
            continue
    print("")
    return val

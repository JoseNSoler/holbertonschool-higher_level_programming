#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format()

    Args:
        value (int): integer to print
    Returns:
        Success - True.
        TypeError or ValueError in value to analyze- False.
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

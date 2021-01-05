#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Function that divides 2 integers
    and prints the result
    Args:
        a: number 1
        b: number 2
    Returns:
        division of all integers on success -
        None in error
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)


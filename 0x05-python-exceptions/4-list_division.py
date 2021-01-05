#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element by element.
    Args:
        my_list_1 (list): first list
        my_list_2 (list): second list
        list_length (int): number of elements to divide
    Returns:
        A new list of length list_length containing all
        the values divisions
    """

    listVal = []
    for x in range(list_length):
        val = 0
        try:
            val = my_list_1[x]/my_list_2[x]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            listVal.append(val)
    return listVal


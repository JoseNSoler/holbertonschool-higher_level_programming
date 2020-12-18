#!/usr/bin/python3
# returns a key with the biggest integer value.


def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    x = max(a_dictionary, key=a_dictionary.get)
    return x

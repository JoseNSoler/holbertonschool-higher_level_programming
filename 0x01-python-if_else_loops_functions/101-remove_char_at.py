#!/usr/bin/python3

def remove_char_at(str, n):
    n_len = len(str)
    n_len = n_len + 1

    for x in range(0, n_len):
        if (n < 0) or (n > n_len):
            return(str)
        if (x == n):
            copy2 = str.replace(str[x], '')
            return(copy2)

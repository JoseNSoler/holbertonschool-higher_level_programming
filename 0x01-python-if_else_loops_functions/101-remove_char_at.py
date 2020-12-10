#!/usr/bin/python3

def remove_char_at(str, n):
    nleno = len(str)
    nleno = nleno + 1

    for x in range(0, nleno):
        if (n < 0) or (n > nleno):
            return(str)
        if (x == n):
            copy2 = str.replace(str[x], '')
            return(copy2)

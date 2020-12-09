#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if(x != " ") and (ord(x) > 96):
            x = chr(ord(x) - 32)
        print(x, end="")
    print()
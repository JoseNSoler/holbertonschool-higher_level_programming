#!/usr/bin/python3
y = 0
for x in range(122, 96, -1):
    if (y == 1):
        x = x - 32
        y = 0
    else:
        y = 1
    print("{}".format(chr(x)), end="")

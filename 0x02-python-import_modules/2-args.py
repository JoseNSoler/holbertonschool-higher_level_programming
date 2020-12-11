#!/usr/bin/python3
import sys
if __name__ == "__main__":
    cadena = str(sys.argv)
    count = len(sys.argv)

    if (count <= 1):
        print("0 arguments.")
    else:
        minus_c = count - 1
        print("{:d} arguments:".format(minus_c))
        for x in range(1, count):
            y = x
            print("{:d}: ".format(y), end='')
            print("{:s}".format(sys.argv[x]))

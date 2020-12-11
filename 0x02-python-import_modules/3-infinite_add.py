#!/usr/bin/python3
import sys

if __name__ == "__main__":
    cadena = sys.argv
    count = len(sys.argv)
    total = 0

    for x in range(1, count):
        numero = int(sys.argv[x])
        total = total + numero
        numero = 0

    print("{:d}".format(total))

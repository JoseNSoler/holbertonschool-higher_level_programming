#!/usr/bin/python3
def add(a, b):
    a = 1
    b = 2
    return(a + b)

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
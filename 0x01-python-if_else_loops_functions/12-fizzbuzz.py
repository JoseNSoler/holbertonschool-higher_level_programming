#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if(x % 5 == 0) and (x % 3 == 0):
            y = "FizzBuzz"
        elif(x % 5 == 0):
            y = "Buzz"
        elif(x % 3 == 0):
            y = "Fizz"
        else:
            y = str(x)
        print("{:s} ".format(y), end="")

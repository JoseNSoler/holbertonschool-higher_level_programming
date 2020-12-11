#!/usr/bin/python3
import sys
if __name__ == "__main__":
    import calculator_1

    values_a = {'+': add, '-': sub, "*": mul, '/': div}

    string = sys.argv
    leno = len(string) - 1
    if(leno < 3) or (leno > 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = sys.argv[2]
    num1, num2, switch = int(string[1]), int(string[3]), 0

    if(leno == 3):
        for x in values_a or switch == 0:
            if(str(string[2]) == x):
                print("{:d} {:s} {:d} = ".format(num1, x, num2), end='')
                print(values_a[x].__call__(num1, num2))
                switch = 1
                break
        if(switch != 1):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    string = sys.argv
    leno = len(string) - 1
    if(leno < 3) or (leno > 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = sys.argv[2]
    num1, num2, switch = int(string[1]), int(string[3]), 0

    if(leno == 3):
        if (sign == '+'):
            print("{:d} + {:d} = {:d}".format(num1, num2, calculator_1.add(num1, num2)))
        elif (sign == '-'):
            print("{:d} + {:d} = {:d}".format(num1, num2, calculator_1.sub(num1, num2)))
        elif (sign == '*'):
            print("{:d} + {:d} = {:d}".format(num1, num2, calculator_1.mul(num1, num2)))
        elif (sign == '/'):
            print("{:d} + {:d} = {:d}".format(num1, num2, calculator_1.div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
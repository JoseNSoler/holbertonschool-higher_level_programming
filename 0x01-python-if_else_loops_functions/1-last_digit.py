#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if (number >= 0):
    last_number = number % 10
else:
    last_number = ((number * -1) % 10) * -1

if last_number > 5:
    string = "and is grater than 5"
elif last_number == 0:
    string = "and is 0"
else:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d} {}".format(number, last_number,string))

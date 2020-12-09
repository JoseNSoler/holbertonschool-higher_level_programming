#!/usr/bin/python3
import random
import sys

number = random.randint(-10000, 10000)
copynum = number
sys.stdout.write("Last digit of %s " % number)

if number < 0:
    number = number * -1

last_number = number % 10

if copynum < 0:
    if last_number is 0:
        sys.stdout.write("is %s " % last_number)
        sys.stdout.write("and is 0")
    else:
        last_number = last_number - (last_number * 2)
        sys.stdout.write("is %s " % last_number)
        sys.stdout.write("and is less than 6 and not 0")

else:
    if last_number > 5:
        sys.stdout.write("is %s " % last_number)
        sys.stdout.write("and is greater than 5")
    else:
        sys.stdout.write("is %s " % last_number)
        sys.stdout.write("and is less than 6 and not 0")
print ('\n')
exit(1)

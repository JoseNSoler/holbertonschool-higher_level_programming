#!/usr/bin/python3
# print all integers on a list
# 

def print_list_integer(my_list=[]):
    for x in range(len(my_list)):
        print("{:d}".format(my_list[x]))

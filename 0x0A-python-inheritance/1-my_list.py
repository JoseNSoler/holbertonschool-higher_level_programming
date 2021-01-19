#!/usr/bin/python3
'''Module - list of available attributes and methods of an object'''


class MyList(list):
    '''Empty rectangle '''

    def print_sorted(self):
        '''Prints My_list in a sorted way '''
        print (sorted(self))

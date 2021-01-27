#!/usr/bin/python3
'''Module- Open, read and print content of a file'''


def read_file(filename=""):
    '''
    Prints in stdout the content of a <filename>
    Args:
        filename: name of file to analyze
    '''

    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            print(line, end='')
    f.closed

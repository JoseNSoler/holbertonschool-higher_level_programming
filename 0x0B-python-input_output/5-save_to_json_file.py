#!/usr/bin/python3
'''Module- Open, read and write a object in JSON on a file'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Write in (file)<filename> a my_obj
    Args:
        my_obj: object to write
        filename: name of file to analyze
    '''

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
    f.close()

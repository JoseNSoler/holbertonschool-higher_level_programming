#!/usr/bin/python3
'''Module- Open, read and create a object based on a JSON file'''

import json


def load_from_json_file(filename):
    '''
    Returns a object based on a JSON file
    Args:
        filename: name of file to analyze
    '''

    with open(filename) as f:
        return json.load(f)

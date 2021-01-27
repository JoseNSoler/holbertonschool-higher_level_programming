#!/usr/bin/python3
'''Module- representation object python of a JSON'''

import json


def from_json_string(my_str):
    '''
    Returns a object python representation of our <my_obj>
    Args:
        my_obj: object to analyze
    '''
    return (json.loads(my_str))

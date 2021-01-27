#!/usr/bin/python3
'''Module- representation JSON of a object python'''

import json


def to_json_string(my_obj):
    '''
    Returns a JSON representation of our <my_obj>
    Args:
        my_obj: object to analyze
    '''
    return (json.dumps(my_obj))

#!/usr/bin/python3
'''Module- Open, read and create a object based on a JSON file'''

import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file



def load_add_save():
    '''
    Returns a object based on a JSON file
    Args:
        filename: name of file to analyze
    '''
    try:
        f_obj = load_from_json_file("add_item.json")
    except FileNotFoundError:
        f_obj = []
    f_obj.extend(sys.argv[1:])
    save_to_json_file(f_obj, "add_item.json")


if __name__ == "__main__":
  load_add_save()

#!/usr/bin/python3
''' Module - Dictionary description with simple data structure '''


def class_to_json(obj):
    '''
    Returns a Dictionary with simple structure data for JSON 
    serialization of a class object
    Args:
        obj: instance object to analize
    '''
    obj_att = obj.__dict__
    return (obj_att)

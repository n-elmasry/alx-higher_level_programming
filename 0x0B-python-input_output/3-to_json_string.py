#!/usr/bin/python3
"""  returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """ returns the JSON representation """
    new_json = json.dumps(my_obj)
    return new_json

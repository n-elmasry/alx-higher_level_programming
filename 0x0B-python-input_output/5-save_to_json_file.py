#!/usr/bin/python3
"""  writes an Object to a text file, using a JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file """
    new_json = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as fle:
        return fle.write(new_json)

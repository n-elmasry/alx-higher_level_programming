#!/usr/bin/python3
"""  creates an Object from a JSON file """
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """
    with open(filename, 'r') as fle:
        new_json = json.load(fle)
        return new_json

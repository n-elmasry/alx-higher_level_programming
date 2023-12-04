#!/usr/bin/python3
"""returns True if the object is an instance of a class, otherwise False"""


def is_same_class(obj, a_class):
    """ returns True or False"""
    if type(obj) is a_class:
        return True
    else:
        return False

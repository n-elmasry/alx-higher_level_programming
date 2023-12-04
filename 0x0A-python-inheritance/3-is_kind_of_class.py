#!/usr/bin/python3
"""True if the object is an instance of a class or subclass,otherwise False"""


def is_kind_of_class(obj, a_class):
    """ returns True or False"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False

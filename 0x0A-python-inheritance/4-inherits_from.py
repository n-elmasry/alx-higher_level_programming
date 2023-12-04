#!/usr/bin/python3
"""True if object is an instance of a class that inherited from the class"""


def inherits_from(obj, a_class):
    """ returns True or False"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

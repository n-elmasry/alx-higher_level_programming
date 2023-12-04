#!/usr/bin/python3
"""  returns the list of available attributes and methods of an object """


def lookup(obj):
    """ lookup function """
    newlist = dir(obj)
    return newlist

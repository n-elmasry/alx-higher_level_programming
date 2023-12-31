#!/usr/bin/python3
"""
Add Integer Module
This module defines a function, add_integer(a, b=98), which adds two numbers.

"""


def add_integer(a, b=98):
    """
    Adds two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)

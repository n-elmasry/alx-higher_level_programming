#!/usr/bin/python3
"""Class LockedClass"""


class LockedClass:
    """Class LockedClass"""
    def __setattr__(self, name, value):
        msg = "'LockedClass' object has no attribute 'last_name'"
        if name != 'first_name':
            raise AttributeError(msg)
        super().__setattr__(name, value)

#!/usr/bin/python3

class LockedClass:
    """Class LockedClass"""
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        super().__setattr__(name, value)

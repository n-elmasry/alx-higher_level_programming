#!/usr/bin/python3
def magic_string():
    magic_string.counter = magic_string.counter + 1 if hasattr(magic_string, 'counter') else 1
    return 'BestSchool' * magic_string.counter

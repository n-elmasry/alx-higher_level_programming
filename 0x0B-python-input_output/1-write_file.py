#!/usr/bin/python3
""" writes a string to a text file, returns the number of characters written"""


def write_file(filename="", text=""):
    """ write to a text file """
    count = len(text)
    with open(filename, 'w', encoding='utf-8') as fle:
        fle.write(text)
        return count

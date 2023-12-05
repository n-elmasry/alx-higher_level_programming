#!/usr/bin/python3
"""  appends a string to text file, returns the number of characters added """


def append_write(filename="", text=""):
    """ appends a string to a text file """
    count = len(text)
    with open(filename, 'a', encoding='utf-8') as fle:
        fle.writelines(text)
    return count

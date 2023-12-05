#!/usr/bin/python3
"""  appends a string at the end of a text file and returns the number of characters added """


def append_write(filename="", text=""):
    """ appends a string to a text file """
    count = len(text)
    with open(filename, 'a', encoding='utf-8') as fle:
        fle.writelines(text)
    return count

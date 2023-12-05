#!/usr/bin/python3
"""  writes a string to a text file and returns the number of characters written """


def write_file(filename="", text=""):
    """ write to a text file """
    with open(filename, 'w', encoding='utf-8') as fle:
        fle.write(text)
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        return len(content) 

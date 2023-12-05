#!/usr/bin/python3
"""  function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ reads a text file """
    with open(filename, "r",  encoding="utf-8") as fle:
        for lines in fle.readlines():
            print(lines, end='')

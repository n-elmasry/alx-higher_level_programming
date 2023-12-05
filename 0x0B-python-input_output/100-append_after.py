#!/usr/bin/python3
""" inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file """
    with open(filename, 'r+') as fle:
        lines = fle.readlines()
        fle.seek(0)
        
        for line in lines:
            fle.write(line)
            if search_string in line:
                fle.write(new_string)
        fle.truncate()

#!/usr/bin/python3
"""   a class MyList that inherits from list """


class MyList(list):
    """ a class MyList """
    def print_sorted(self):
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)

#!/usr/bin/python3
"""   a class MyList that inherits from list """


class MyList(list):
    """ a class MyList """

    def print_sorted(self):
        sortedlist = sorted(self)
        print(sortedlist)

#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def x(num):
        return num * number
    new_list = []
    new_list = list(map(x, my_list))
    return new_list

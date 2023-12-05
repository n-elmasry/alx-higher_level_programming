#!/usr/bin/python3
"""  class Student that defines a student """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        newdict = {}

        if isinstance(attrs, list):
            for atrr in atrrs:
                if hasattr(self, attr):
                    newdict[atrr] = getattr(self, attr)

        else:
            newdict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
        return newdict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

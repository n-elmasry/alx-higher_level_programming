#!/usr/bin/python3
""" to manage id attribute in all the future classes """
import json
import os


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init funf """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # json static method
    @staticmethod
    def to_json_string(list_dictionaries):
        """ json static method """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            newstring = json.dumps(list_dictionaries)
        return newstring

    # class methos save_to_file
    @classmethod
    def save_to_file(cls, list_objs):
        """ class methos save_to_file """
        filename = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(string))

    # static method from_json_string
    @staticmethod
    def from_json_string(json_string):
        """ static method from_json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            new_list = json.loads(json_string)
        return new_list

    # class method create
    @classmethod
    def create(cls, **dictionary):
        """ class method create """
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    # calss method load_from_file
    @classmethod
    def load_from_file(cls):
        """ calss method load_from_file """
        filename = f'{cls.__name__}.json'
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            jsonstring = f.read()

        data = cls.from_json_string(jsonstring)

        newlist = [cls.create(**item) for item in data]
        return newlist

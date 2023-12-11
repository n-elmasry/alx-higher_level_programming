#!/usr/bin/python3
""" to manage id attribute in all the future classes """
import json
import os


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # json static method
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            newstring = json.dumps(list_dictionaries)
        return newstring

    # class methos save_to_file
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None or len(list_objs) == 0:
            jsstring = "[]"
        else:
            jsstring = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )
            with open(f'{cls.__name__}.json', 'w') as f:
                f.write(jsstring)

    # static method from_json_string
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            new_list = json.loads(json_string)
        return new_list

    # class method create
    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    # calss method load_from_file
    @classmethod
    def load_from_file(cls):
        filename = f'{cls.__name__}.json'
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            jsonstring = f.read()

        data = cls.from_json_string(jsonstring)

        newlist = [cls.create(**item) for item in data]
        return newlist

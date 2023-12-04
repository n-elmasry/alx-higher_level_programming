#!/usr/bin/python3
""" a class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""subclass """


class Rectangle(BaseGeometry):

    def __init__(self, width, height):

        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

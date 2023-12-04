#!/usr/bin/python3
""" a class BaseGeometry """


class BaseGeometry:
    """ a class BaseGeometry """
    def __init__(self) -> None:
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


"""subclass """


class Rectangle(BaseGeometry):

    def __init__(self, width, height):

        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

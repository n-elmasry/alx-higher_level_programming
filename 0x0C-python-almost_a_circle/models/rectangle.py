#!/usr/bin/python3
""" Class Rectangle inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # getters and setters
    @property
    def width(self):
        """ width """
        return (self.__width)

    # width setter
    @width.setter
    def width(self, value):
        """ width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # height
    @property
    def height(self):
        """ height """
        return (self.__height)

    # height setter
    @height.setter
    def height(self, value):
        """ height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # x getter
    @property
    def x(self):
        """ x getter """
        return (self.__x)

    # x setter
    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # y getter
    @property
    def y(self):
        """ y setter """
        return (self.__y)

    # y setter
    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    # public method area
    def area(self):
        """ area method """
        return self.__height * self.__width

    # print rectangle
    def display(self):
        """ display method """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    # override method
    def __str__(self):
        """ override method """
        msg = (f'[Rectangle] ({self.id}) '
               f'{self.__x}/{self.__y} - {self.width}/{self.height}')
        return msg

    # update public method
    def update(self, *args, **kwargs):
        """ update method """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    # dictionary public method
    def to_dictionary(self):
        """ to dictionary method """
        my_dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return my_dict

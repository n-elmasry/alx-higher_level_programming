#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ class Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    # width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
    # area

    def area(self):
        return self.__width * self.__height
    # perimeter

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)
    # override function

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)
            if i < self.__height - 1:
                result += '\n'
        return result

    def __repr__(self):
        return f" Rectangle({self.width,self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        result1 = rect_1.area()
        result2 = rect_2.area()
        if result1 >= result2:
            return rect_1
        elif result1 < result2:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

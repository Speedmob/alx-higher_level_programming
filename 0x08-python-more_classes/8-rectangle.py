#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A class that defines a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle

        Args:
           width (int): Width of Rectange
           height (int): Height of Rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if not self.__width or not self.__height:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if not self.__width or not self.__height:
            return ("")
        rectstr = []
        for x in range(self.__height):
            for y in range(self.__width):
                rectstr.append(str(self.print_symbol))
            if x != self.__height - 1:
                rectstr.append("\n")
        return ("".join(rectstr))

    def __repr__(self):
        w = self.__width
        h = self.__height

        return ("Rectangle({}, {})".format(w, h))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

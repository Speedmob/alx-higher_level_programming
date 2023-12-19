#!/usr/bin/python3
"""a MagicClass matching exactly a bytecode."""
import math


class MagicClass:
    """a circle."""

    def __init__(self, radius=0):
        """MagicClass initializator.

        Arg:
            radius (float or int): radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)

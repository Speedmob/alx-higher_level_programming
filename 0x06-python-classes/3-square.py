#!/usr/bin/python3
"""Define a square class."""


class Square:
    """a square."""
    def __init__(self, size=0):
        """a Square initializer.

        Args:
            size (int): square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns size of square"""
        return self.__size ** 2

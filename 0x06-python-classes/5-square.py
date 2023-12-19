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

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value of size

        Args:
            value (int): new square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with # as representation."""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

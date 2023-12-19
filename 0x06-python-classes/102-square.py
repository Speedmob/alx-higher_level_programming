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

    def __eq__(self, other):
        """== comparision of a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= comparison of a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """< comparison of a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """<= comparison of a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> comparison of a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= compmarison of a Square."""
        return self.area() >= other.area()

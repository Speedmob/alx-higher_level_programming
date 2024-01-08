#!/usr/bin/python3
"""A class MyInt that inherits from int class."""


class MyInt(int):
    """A class that inverts int operators == and !=."""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value

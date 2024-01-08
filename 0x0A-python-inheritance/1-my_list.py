#!/usr/bin/python3
"""An inherited list class MyList."""


class MyList(list):
    """A class that prints the result of the sorted algorithm"""

    def print_sorted(self):
        """A function that print a list in sorted ascending order."""
        print(sorted(self))

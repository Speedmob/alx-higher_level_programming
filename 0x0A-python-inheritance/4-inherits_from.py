#!/usr/bin/python3
"""A class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of the specified class.

    Args:
        obj (any): object to check.
        a_class (type): class to match.
    Returns:
        An inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

#!/usr/bin/python3
"""A class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of the specified class.

    Args:
        obj (any): object to check.
        a_class (type): class to match.
    Returns:
        An instance/inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False

#!/usr/bin/python3
"""A function that adds an attribute to an object."""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (any): object.
        att (str): attribute.
        value (any): value of attribute.
    Raises:
        TypeError: attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

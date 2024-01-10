#!/usr/bin/python3
"""a Python class-to-JSON function."""


def class_to_json(obj):
    """creates a dictionary represntation of a data structure."""
    return obj.__dict__

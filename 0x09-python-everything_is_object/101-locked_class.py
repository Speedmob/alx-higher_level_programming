#!/usr/bin/python3
"""Defines a LockedClass."""


class LockedClass:
    """
    Prevent the user from creating new instance attributes
    except an attribute called 'first_name'.
    """

    __slots__ = ["first_name"]

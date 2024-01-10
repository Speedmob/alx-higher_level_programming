#!/usr/bin/python3
"""a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """creates a JSON representation of a string obj."""
    return json.dumps(my_obj)

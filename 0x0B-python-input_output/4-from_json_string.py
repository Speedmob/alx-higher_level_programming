#!/usr/bin/python3
"""a JSON-to-string function."""
import json


def from_json_string(my_str):
    """creates a python string representation of a JSON string."""
    return json.loads(my_str)

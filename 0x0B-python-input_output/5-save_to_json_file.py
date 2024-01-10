#!/usr/bin/python3
"""a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON representation of a string obj to a textfile."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

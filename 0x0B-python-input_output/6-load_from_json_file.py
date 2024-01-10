#!/usr/bin/python3
"""a JSON file reading function."""
import json


def load_from_json_file(filename):
    """reads from a JSON file."""
    with open(filename) as f:
        return json.load(f)

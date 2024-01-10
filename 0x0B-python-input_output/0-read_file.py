#!/usr/bin/python3
"""textfile reading function."""


def read_file(filename=""):
    """reads a textfile and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

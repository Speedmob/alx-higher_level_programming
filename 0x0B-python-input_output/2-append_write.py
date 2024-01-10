#!/usr/bin/python3
"""textfile appending function."""


def append_write(filename="", text=""):
    """Appends a string at end of a UTF8 textfile.

    Args:
        filename (str): textfile to append to.
        text (str): string to append to textfile.
    Returns:
        num of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

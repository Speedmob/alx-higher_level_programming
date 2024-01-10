#!/usr/bin/python3
"""textfile writing function."""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF8 textfile.

    Args:
        filename (str): filename.
        text (str): text to write.
    Returns:
        num of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

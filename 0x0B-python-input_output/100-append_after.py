#!/usr/bin/python3
"""a textfile insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing a given string in a file.

    Args:
        filename (str): name of the file.
        search_string (str): given string.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)

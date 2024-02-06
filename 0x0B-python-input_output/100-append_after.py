#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        search_string (str, optional): The string to search for. Defaults to "".
        new_string (str, optional): The string to append. Defaults to "".
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        i = 0
        while i < len(text):
            fo.write(text[i])
            if search_string in text[i]:
                fo.write(new_string)
            i += 1

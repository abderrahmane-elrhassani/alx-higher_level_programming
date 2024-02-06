#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file encoded in UTF-8 and returns the count
    of characters added.

    Parameters:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The string of text to append to the file. Defaults to "".

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """
        This function returns the number of characters appended to the file.
        """
        return f.write(text)

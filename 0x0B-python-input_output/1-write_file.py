#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file encoded in UTF-8 and returns the count
    of characters written.

    Parameters:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The string of text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """
        This function returns the number of characters written to the file.
        """
        return f.write(text)

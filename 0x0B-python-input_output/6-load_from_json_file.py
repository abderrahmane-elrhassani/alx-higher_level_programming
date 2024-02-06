#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json


def save_to_json_file( filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        filename (str): The name of the file.

    Returns:
        type: The JSON representation.
    """

    with open(filename) as f:
        return json.load(f)

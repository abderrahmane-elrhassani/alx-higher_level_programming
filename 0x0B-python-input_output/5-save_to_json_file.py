#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj (type): The object to write to the text file.
        filename (str): The name of the file.

    Returns:
        type: The JSON representation.
    """

    # Writing to the file
    with open(filename, 'w', encoding="utf-8") as f:
        # Serializing JSON
        json_object = json.dumps(my_obj)
        # or json.dump(my_obj, f)
        f.write(json_object)
        f.close()

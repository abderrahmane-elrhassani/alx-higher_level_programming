#!/usr/bin/python3
"""Module containing the function to_json_string"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (type): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    # Serializing the object to JSON
    return json.dumps(my_obj)

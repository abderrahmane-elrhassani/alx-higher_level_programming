#!/usr/bin/python3
"""Module containing the function from_json_string"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        type: The Python object obtained from the JSON string.
    """
    
      
    # Deserializing the JSON string to a Python object
    return json.loads(my_str)

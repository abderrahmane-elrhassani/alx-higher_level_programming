#!/usr/bin/python3
"""Defines a function named lookup()"""


def lookup(obj):
    """Returns a list of available attributes and methods for an object.

    Args:
        obj (class): The object for which attributes and methods are to be looked up.

    Returns:
        list: A list of available attributes and methods of the given object.
    """
    return dir(obj)

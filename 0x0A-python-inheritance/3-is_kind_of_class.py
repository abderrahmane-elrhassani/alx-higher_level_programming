#!/usr/bin/python3
"""Defines a class and an inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
        
    Returns:
        True if obj is an instance or inherited instance of a_class, False otherwise.
    """
    while not isinstance(obj, a_class):
        return False
    return True

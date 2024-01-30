#!/usr/bin/python3
"""Defines the LockedClass class"""


class LockedClass:
    """
    This class restricts the dynamic creation of new instance attributes,
    allowing only the attribute 'first_name' to be added.

    Attributes:
        first_name (str): The first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of the LockedClass."""
        self.first_name = "first_name"

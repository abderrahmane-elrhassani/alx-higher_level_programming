#!/usr/bin/python3
"""Defines a custom list class MyList, inheriting from the built-in list class."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))

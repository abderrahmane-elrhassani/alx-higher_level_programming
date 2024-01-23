#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """
    This class defines the properties of a square, based on the 0-square.py file.

    Attributes:
        size (int): The size of the square (one side).
    """

    def __init__(self, size):
        """
        Initializes new instances of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

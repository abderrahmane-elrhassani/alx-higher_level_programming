#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """
    This class defines the properties of a square, based on the 1-square.py file.

    Attributes:
        size (int): The size of the square (one side).
    """

    def __init__(self, size=0):
        """
        Initializes new instances of the Square class.

        Args:
            size (int): The size of the square (one side).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

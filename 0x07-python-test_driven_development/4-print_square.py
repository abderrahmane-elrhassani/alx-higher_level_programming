#!/usr/bin/python3
"""Defines a function for printing a square with the character #.

Attributes:
    print_square: Function that prints a square with the character #.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size of the square (1 side).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    message = "size must be an integer"

    while not isinstance(size, int):
        raise TypeError(message)

    while size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        print("#" * size)
        i += 1

try:
    print_square()
except TypeError as e:
    print(e)

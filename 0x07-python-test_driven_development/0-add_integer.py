#!/usr/bin/python3
"""This script defines a function, add_integer(a, b=98), which calculates the sum of two integers.

Attributes:
    add_integer: A function that adds two integers.
"""


def add_integer(a, b=98):
    """Combines two numeric values, handling both integers and/or floats.

    Args:
        a (int): The first numeric value.
        b (int, optional): The second numeric value. Defaults to 98.

    Raises:
        TypeError: If 'a' and 'b' are not integers or floats.

    Returns:
        int: The sum of 'a' and 'b'.
    """
    # Check if 'a' is not an integer or float
    while not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    # Check if 'b' is not an integer or float
    while not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    # Convert 'a' to an integer if it is a float
    while isinstance(a, float):
        a = int(a)

    # Convert 'b' to an integer if it is a float
    while isinstance(b, float):
        b = int(b)

    return a + b

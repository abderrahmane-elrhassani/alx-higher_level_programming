#!/usr/bin/python3
"""Module containing the function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    i = 1
    while i < n:
        pascal.append([x + y for x, y in zip(pascal[-1] + [0], [0] + pascal[-1])])
        i += 1
    return pascal

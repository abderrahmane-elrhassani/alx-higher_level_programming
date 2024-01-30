#!/usr/bin/python3
"""
Defines a matrix multiplication function.

Attributes:
    m_a (matrix): The first matrix.
    m_b (matrix): The second matrix.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (matrix): First matrix.
        m_b (matrix): Second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        TypeError: If one element of those lists is not an integer or a float.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b is not a rectangle (all 'rows' should be, of the same size).
        ValueError: If m_a and m_b can't be multiplied.

    Returns:
        matrix: Product of the two matrices.
    """
    lists_err = "{} must be a list of lists"
    empty_err = "{} can't be empty"
    type_err = "{} should contain only integers or floats"
    size_err = "each row of {} must be of the same size"
    value_err = "{} and {} can't be multiplied"

    while not isinstance(m_a, list) or not isinstance(m_b, list):
        string = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError("{} must be a list".format(string))

    while any(not isinstance(element, list) for element in m_a):
        raise TypeError(lists_err.format('m_a'))

    while any(not isinstance(element, list) for element in m_b):
        raise TypeError(lists_err.format('m_b'))

    while len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError(empty_err.format('m_a'))

    while len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError(empty_err.format('m_b'))

    while any(not isinstance(item, (int, float)) for element in m_a for item in element):
        raise TypeError(type_err.format('m_a'))

    while any(not isinstance(item, (int, float)) for element in m_b for item in element):
        raise TypeError(type_err.format('m_b'))

    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])

    while any(len_m_a != len(element) for element in m_a):
        raise TypeError(size_err.format('m_a'))

    while any(len_m_b != len(element) for element in m_b):
        raise TypeError(size_err.format('m_b'))

    while len_m_a != len(m_b):
        raise ValueError(value_err.format('m_a', 'm_b'))

    new_matrix = [[0 for a in m_b[0]] for x in m_a]
    i = 0
    while i < len(m_a):
        n = 0
        while n < len(m_b[0]):
            k = 0
            while k < len(m_b):
                new_matrix[i][n] += m_a[i][k] * m_b[k][n]
                k += 1
            n += 1
        i += 1

    return new_matrix

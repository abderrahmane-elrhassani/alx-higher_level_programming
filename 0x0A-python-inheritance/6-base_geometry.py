#!/usr/bin/python3
"""Defines a class BaseGeometry, based on 5-base_geometry.py"""


class BaseGeometry:
    """BaseGeometry class.
    """
    def area(self):
        """Calculates the area.

        Raises:
            Exception: If area is not implemented.
        """
        raise Exception("area() is not implemented")

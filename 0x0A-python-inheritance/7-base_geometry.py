#!/usr/bin/python3
"""Defines a class BaseGeometry, based on 6-base_geometry.py"""


class BaseGeometry:
    """BaseGeometry class.
    """
    def area(self):
        """Calculates the area.

        Raises:
            Exception: If area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.

        Args:
            name (str): Name of the object.
            value (int): Value of the property.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        while not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        while value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

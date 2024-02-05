#!/usr/bin/python3
"""Defines a class Rectangle, based on 7-base_geometry.py.

Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Creates new instances of Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

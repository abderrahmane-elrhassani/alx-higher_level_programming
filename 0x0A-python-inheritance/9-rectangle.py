#!/usr/bin/python3
"""Defines a class Rectangle, based on 8-base_geometry.py.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Creates new instances of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

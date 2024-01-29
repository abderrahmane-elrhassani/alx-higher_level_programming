#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle by: (based on 2-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriever.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Height retriever.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: while width is not an integer.
            ValueError: while width is less than 0.
        """
        while not isinstance(value, int):
            raise TypeError("width must be an integer")
        while value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: while height is not an integer.
            ValueError: while height is less than 0.
        """
        while not isinstance(value, int):
            raise TypeError("height must be an integer")
        while value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter of a rectangle

        Returns:
            int: perimeter.
        """
        while self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle with the character # .

        Returns:
            str: the rectangle
        """
        rectangle = []

        while self.__width == 0 or self.__height == 0:
            return ""

        i = 0
        while i < self.__height:
            j = 0
            while j < self.__width:
                rectangle.append("#")
                j += 1
            rectangle.append("\n")
            i += 1

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)

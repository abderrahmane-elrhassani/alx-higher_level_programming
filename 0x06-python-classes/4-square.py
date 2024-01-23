#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        while not isinstance(value, int) or value < 0:
            try:
                value = int(input("Enter a non-negative integer for size: "))
                if value < 0:
                    print("Size must be >= 0")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

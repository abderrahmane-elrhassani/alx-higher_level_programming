#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        while not isinstance(size, int) or size < 0:
            try:
                size = int(input("Enter a non-negative integer for size: "))
                if size < 0:
                    print("Size must be >= 0")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

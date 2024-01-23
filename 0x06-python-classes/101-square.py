#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.SIZE = size
        self.POSITION = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.SIZE

    @size.setter
    def size(self, value):
        while not isinstance(value, int) or value < 0:
            try:
                value = int(input("Enter a non-negative integer for size: "))
                if value < 0:
                    print("Size must be >= 0")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        self.SIZE = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.POSITION

    @position.setter
    def position(self, value):
        while (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            try:
                value = eval(input("Enter a tuple of 2 positive integers for position: "))
                if (
                    not isinstance(value, tuple)
                    or len(value) != 2
                    or not all(isinstance(num, int) for num in value)
                    or not all(num >= 0 for num in value)
                ):
                    print("Invalid input. Please enter a tuple of 2 positive integers.")
            except:
                print("Invalid input. Please enter a valid tuple.")
        self.POSITION = value

    def area(self):
        """Return the current area of the square."""
        return self.SIZE * self.SIZE

    def my_print(self):
        """Print the square with the # character."""
        if self.SIZE == 0:
            print("")
            return

        [print("") for s in range(0, self.POSITION[1])]
        for s in range(0, self.SIZE):
            [print(" ", end="") for l in range(0, self.POSITION[0])]
            [print("#", end="") for m in range(0, self.SIZE)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.SIZE != 0:
            [print("") for s in range(0, self.POSITION[1])]
        for s in range(0, self.SIZE):
            [print(" ", end="") for l in range(0, self.POSITION[0])]
            [print("#", end="") for m in range(0, self.SIZE)]
            if s != self.SIZE - 1:
                print("")
        return ("")

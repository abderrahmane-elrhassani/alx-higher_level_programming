#!/usr/bin/python3
"""Module defining the class Student"""


class Student:
    """
    Class defining properties of a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (int): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student.

        Args:
            first_name (str): The first name of the student.
            last_name (int): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation.
        """
        return self.__dict__

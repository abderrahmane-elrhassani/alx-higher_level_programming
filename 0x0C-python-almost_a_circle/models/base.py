#!/usr/bin/python3
"""Defines a class Base"""

class Base:
    '''A representation of the base of our OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        while id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

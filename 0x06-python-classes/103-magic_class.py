#!/usr/bin/python3
"""
This module defines class MagicClass
"""
import math


class MagicClass:
    """
    This class does exactly the same as the given Python bytecode
    """
    def __init__(self, radius=0):
        """
        constructor
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

        return None

    def area(self):
        """
        Return the area
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Return the circumference
        """
        return 2 * math.pi * self.__radius

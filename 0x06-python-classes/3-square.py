#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    This class is a class to define suare object
    """
    def __init__(self, size=0):
        """initialization function (constructor)
            size (integer): square size
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Return the current square area
        """
        return (self.__size ** 2)

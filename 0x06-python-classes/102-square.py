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
        if type(size) != int and type(size) != float:
            raise TypeError('size must be a number')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Return the current square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        getter for size attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter for size attribute
        """
        if type(value) != int and type(value) != float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __lt__(self, other):
        return self.__size < other.size

    def __le__(self, other):
        return self.__size <= other.size

    def __eq__(self, other):
        return self.__size == other.size

    def __ne__(self, other):
        return self.__size != other.size

    def __gt__(self, other):
        return self.__size > other.size

    def __ge__(self, other):
        return self.__size >= other.size

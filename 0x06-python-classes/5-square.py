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
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if (sef.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print("#" * sel.__size)

#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    This class is a class to define suare object
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialization function (constructor)
            size (integer): square size
            position (tuple): square position
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if len(position) == 2:
            if (type(position[0]) == int and
                    type(position[1]) == int):
                if (position[0] >= 0 and position[1] >= 0):
                    self.__position = position
                else:
                    raise TypeError("position must be a "
                                    "tuple of 2 positive integers")
            else:
                raise TypeError("position must be a "
                                "tuple of 2 positive integers")
        else:
            raise TypeError("position must be a "
                            "tuple of 2 positive integers")

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

    @property
    def position(self):
        """
        getter for position attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        setter for position attribute
        """
        if len(value) == 2:
            if (type(value[0]) == int and type(value[1]) == int):
                if (value[0] >= 0 and value[1] >= 0):
                    self.__position = value
                else:
                    raise TypeError("position must be a tuple "
                                    "of 2 positive integers")
            else:
                raise TypeError("position must be a tuple "
                                "of 2 positive integers")
        else:
            raise TypeError("position must be a tuple  "
                            "of 2 positive integers")

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("{}{}".format(" " * self.__position[0],
                                    "#" * self.__size))

    def __repr__(self):
        """
        string representation of the object
        """
        string = ""
        for j in range(self.__position[1]):
            string += "\n"
        for i in range(self.__size):
            string += " " * self.__position[0]
            string += "#" * self.__size)
        return string

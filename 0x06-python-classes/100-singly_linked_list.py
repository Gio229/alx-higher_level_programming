#!/usr/bin/python3
"""
This module define a class Node and class SinglyLinkedList
"""


class Node:
    """
    defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """initialization function (constructor)
            data (integer)
            next_node (Node): square position
        """
        if (type(data) != int):
            raise TypeError("data must be an integer")
        self.__data = data

        if (type(next_node) == Node or next_node is None):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """
        getter for data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter for data attribute
        """
        if (type(data) != int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        getter for next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for next_node attribute
        """
        if (type(value) == Node or value is None):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    This class define a singly linked list
    """
    def __init__(self):
        """initialization function (constructor)
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position in
        the list
        """
        if (self.__head is None):
            self.__head = Node(value)
        else:
            current = self.__head
            previous = current
            while current.next_node is not None:
                if (value <= current.data):
                    break
                previous = current
                current = current.next_node
            if current is self.__head:
                if (value <= current.data):
                    self.__head = Node(value, current)
                elif current.next_node is None:
                    current.next_node = Node(value)
            elif current.next_node is None:
                if (current.data < value):
                    current.next_node = Node(value)
                else:
                    newNode = Node(value, current)
                    previous.next_node = newNode
            else:
                newNode = Node(value, current)
                previous.next_node = newNode

    def __repr__(self):
        """
        string representation of the class
        """
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data)
            current = current.next_node
            if current is not None:
                string += '\n'

        return string

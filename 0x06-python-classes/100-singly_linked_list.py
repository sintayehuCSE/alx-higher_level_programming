#!/usr/bin/python3
"""Define class Node and SinglyLinkedList."""


class Node:
    """The node of singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize the data and next node pointer of a node.


        Args:
            data (int): The data of the node.
            next_node (Node): Pointer to next node of the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/return the data of specific node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/return the next_node of the list."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Represent a singly linked list."""
    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the SinglyLinkedList.
        The node is inserted into the list at the correct ordered numerical
        position.


        Args:
            value (int): The integer data of new Node
        """
        new_node = Node(value)
        if not self.__head:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node) and (temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        value = []
        temp = self.__head
        while (temp):
            value.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(value))

#!/usr/bin/python3

"""
Module for implementing a singly linked list and its nodes.
"""


class Node:
    """
    Class for representing a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): A reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None) -> None:
        """
        Initialize a new node with the given data and next node reference.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): A reference to the next node in
            the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        """
        int: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value) -> None:
        """
        Set the data of the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Node: A reference to the next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value) -> None:
        """
        Set the next node reference of the node.

        Args:
            value (Node): A reference to the next node in the linked list.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Class for representing a singly linked list.

    Attributes:
        head (Node): A reference to the first node in the linked list.
    """
    def __init__(self):
        """
        Initialize a new empty singly linked list.
        """
        self.head = None

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Insert a new node with the given value into the correct
        sorted position in the linked list.

        Args:
            value (int): The value to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        if current_node.data > value:
            new_node.next_node = current_node
            self.head = new_node
            return

        while (current_node.next_node is not None and
               current_node.next_node.data < value):
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

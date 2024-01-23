#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """
    Class that defines properties Node.

    Attributes:
        DATA: data field of node.
    """
    def __init__(self, data, next_node=None):
        """Creates new instances of node.

        Args:
            data : data field of node.
        """
        self.DATA = data
        self.NEXT_NODE = next_node

    @property
    def data(self):
        """Retrieves the data field instance.

        Returns: the data field of a node.
        """
        return self.DATA

    @data.setter
    def data(self, value):
        """Propery setter for data.

        Args:
            value (int): data field of a node.

        Raises:
            TypeError: DATA must be an integer
        """
        while not isinstance(value, int):
            try:
                value = int(input("Enter an integer for data: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        self.DATA = value

    @property
    def next_node(self):
        """Retrives the next_node instance.

        Returns: The next_node instance.
        """
        return self.NEXT_NODE

    @next_node.setter
    def next_node(self, value):
        """Property setter for Node.

        Args:
            value (None): next node of a Node.

        Raises:
            TypeError: NEXT_NODE must be a Node object.
        """
        while value is not None and not isinstance(value, Node):
            try:
                value = int(input("Enter a Node object for next_node: "))
            except ValueError:
                print("Invalid input. Please enter a Node object.")
        self.NEXT_NODE = value


class SinglyLinkedList:
    """
    Class that defines properties of SinglyLinkedList.

    Attributes:
        HEAD: head of the SinglyLinkedList.
    """
    def __init__(self):
        """Creates new instances of SinglyLinkedList .

        Args:
            head : head of the SinglyLinkedList .
        """
        self.HEAD = None

    def __str__(self):
        """Represents the class objects as a string.

        Returns: The class object represented as a string.
        """
        temp_var = self.HEAD
        print_node = []
        while temp_var:
            print_node.sort()
            print_node.append(str(temp_var.DATA))
            temp_var = temp_var.NEXT_NODE

        print_node.sort(key=int)
        return "\n".join(print_node)

    def sorted_insert(self, value):
        """Inserts a new node at a given position.

        Args:
            value: value.
        """
        if self.HEAD is None:
            new_node = Node(value)
            new_node.NEXT_NODE = self.HEAD
            self.HEAD = new_node
        else:
            new_node = Node(value)
            new_node.DATA = value
            new_node.NEXT_NODE = self.HEAD
            self.HEAD = new_node

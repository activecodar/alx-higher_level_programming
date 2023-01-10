#!/usr/bin/python3

"""
Module for creating custom list classes.

This module provides a class that inherits
from the built-in list class and adds a method for
printing a sorted version of the list.
"""


class MyList(list):
    """
    Custom list class.
    This class inherits from the built-in list
    class and adds a method for printing a sorted version of the list.
    """

    def print_sorted(self):
        """
        Prints a sorted version of the list.
        The list is sorted in ascending order.
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)

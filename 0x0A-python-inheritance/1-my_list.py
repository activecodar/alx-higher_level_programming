#!/usr/bin/python3
"""Module for creating custom list classes"""


class MyList(list):
    """This class inherits from the built-in list"""

    def print_sorted(self):
        """Prints a sorted version of the list"""
        print(sorted(self))

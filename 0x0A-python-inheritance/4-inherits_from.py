#!/usr/bin/python3
"""
This module contains a function that checks if an object is
an instance of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of
    a class that inherited from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to check inheritance from.

    Returns:
        bool: True if the object is an instance of
        a class that inherited from the specified class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3

"""
Module for checking class equality.

This module provides a function for determining
whether an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an
    instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance
        of the specified class, False otherwise.
    """
    return type(obj) == a_class

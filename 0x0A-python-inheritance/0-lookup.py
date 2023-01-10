#!/usr/bin/python3

"""
Module for inspecting objects.

This module provides a function for returning a
list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes
    and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes
        and methods of the object.
    """
    # Get all attributes and methods of the object
    attributes_and_methods = dir(obj)
    # Filter out built-in methods
    return [attr for attr in attributes_and_methods]

#!/usr/bin/python3
"""
Module for getting dictionary representation of object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary containing the serializable
              attributes of a given class instance
    """
    return obj.__dict__

#!/usr/bin/python3
"""
Module for converting an object to json representation
"""
import json


def to_json_string(my_obj):
    """
    Convert an object to json representation.

    Args:
        my_obj : The object that needs to be converted to json

    Returns:
        str: json representation of the object
    """
    return json.dumps(my_obj)

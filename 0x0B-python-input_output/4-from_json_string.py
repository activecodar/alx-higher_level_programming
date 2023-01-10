#!/usr/bin/python3
"""
Module for converting a json representation to an object
"""
import json


def from_json_string(my_str):
    """
    Convert json representation of an object to the object itself

    Args:
        my_str: json representation of the object

    Returns:
        object: the object represented by the json string
    """
    return json.loads(my_str)

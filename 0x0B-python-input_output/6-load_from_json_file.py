#!/usr/bin/python3
"""
Module for creating an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a json file

    Args:
        filename (str):path and filename of the json file

    Returns:
        object :object represented by json file
    """
    with open(filename, 'r') as f:
        return json.load(f)

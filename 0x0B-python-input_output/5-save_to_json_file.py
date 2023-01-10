#!/usr/bin/python3
"""
Module for writing an object to a json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using json representation

    Args:
        my_obj: object that needs to be written to json file
        ilename (str): path and filename where the json file
                       should be written

    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

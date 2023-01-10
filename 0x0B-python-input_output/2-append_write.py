#!/usr/bin/python3
"""
Module for appending text to a file and
returning the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text
    file and returns the number of characters added

    Args:
        filename (str): The path and name of the file
        text (str): The string to be added to the file

    Returns:
        int : The number of characters added to the file
    """
    with open(filename, 'a', encoding='utf8') as f:
        f.write(text)
    return len(text)

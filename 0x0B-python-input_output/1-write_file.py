#!/usr/bin/python3
"""
Module for writing text files.

This module provides a single function `write_file`
for writing a text string to a text file and returning
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and
    returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.

    Raises:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_chars = f.write(text)
    return num_chars

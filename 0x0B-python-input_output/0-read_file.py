#!/usr/bin/python3
"""
Module for reading text files.

This module provides a single function `read_file`
for reading a text file and printing its contents
to the standard output.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to the standard output.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    Returns:
        None

    Raises:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.read()
    print(line, end="")
    f.close()

#!/usr/bin/python3
"""
Module for printing a string with the first and last name.

This module provides a single function, `say_my_name`,
which takes a first name and a last name as input and prints a
string with the first and last name. If either input is not a string,
a `TypeError` is raised.

Examples:
    >>> say_my_name('John', 'Doe')
    My name is John Doe
    >>> say_my_name('Jane')
    My name is Jane

"""


def say_my_name(first_name, last_name=""):
    """Prints a string with the first and last name.

    Args:
      first_name: A string.
      last_name: A string. Default is an empty string.

    Raises:
      TypeError: If first_name or last_name is not a string.

    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    # Print the string with the first and last name
    print(f'My name is {first_name} {last_name}')

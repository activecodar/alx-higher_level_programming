#!/usr/bin/python3
"""
Module for adding two integers.
Provides function, `add_integer`, which adds two
integers and returns the result as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
      a: An integer or float.
      b: An integer or float. Default is 98.

    Raises:
      TypeError: If a or b is not an integer or float.

    Returns:
      The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or float')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or float')
    return int(a) + int(b)

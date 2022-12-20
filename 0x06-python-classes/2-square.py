#!/usr/bin/python3
"""
This module contains a class for representing squares in two-dimensional space.
The Square class provides methods for calculating the area and perimeter
of a square,and has an attribute for storing the side length of the square.
"""


class Square:
    """
    A square is a polygon with four equal sides and four right angles.

    This class represents a square in two-dimensional space.
    Attributes:
        side_length (float): The length of a side of the square.
    """
    def __init__(self, size: int = 0) -> None:
        """Initialize a Square object.

        Args:
            size (int, optional): The length of a side of the square.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3
"""
This module contains a base class for
geometry objects.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a square object.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2

#!/usr/bin/python3
"""
This module contains a base class for
geometry objects.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square defining class
    """

    def __init__(self, size):
        """
        Initialize a square object.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

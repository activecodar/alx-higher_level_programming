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
        """
        Initialize a Square object.

        Args:
            size (int, optional): The length of a side of the square.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """
        Calculate the area of the square.

        Returns:
            The area of the square (units^2).
        """
        return self.__size**2

    @property
    def size(self) -> int:
        """
        Get the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def my_print(self) -> None:
        """
        Print the square to the console.

        The square is printed using the character "#".
        If the size of the square is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

#!/usr/bin/python3
"""
This module contains a base class for
geometry objects.
"""


class BaseGeometry:
    """
    A base class for geometry objects.
    """

    def area(self):
        """
        Calculate the area of the geometry object.

        Raises:
            NotImplementedError: If the area is not
            implemented for the specific geometry object.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a given value.

        Args:
            name (str): The name of the value to validate.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if int(value) <= 0:
            raise ValueError(f"{name} must be greater than 0")

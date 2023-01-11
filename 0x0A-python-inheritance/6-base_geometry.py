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
            NotImplementedError: If the area is
            not implemented for the specific geometry object.
        """
        raise Exception("area() is not implemented")

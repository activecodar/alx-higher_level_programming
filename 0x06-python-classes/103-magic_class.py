"""
Module for implementing a magic class that
can perform some calculations on circles.
"""

import math


class MagicClass:
    """
    Class for representing a circle and performing some calculations
    on it.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius=0):
        """
        Initialize a new circle with the given radius.

        Args:
            radius (float, optional): The radius of the circle.
            Defaults to 0.

        Raises:
            TypeError: If the radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        """
        float: The radius of the circle.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Set the radius of the circle.

        Args:
            value (float): The new radius of the circle.

        Raises:
            TypeError: If the value is not a number.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

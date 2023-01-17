#!/usr/bin/python3
"""
This module contains the Rectangle class, which inherits
from the Base class and represents a rectangle object.
from models.base import Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base

    Args:
    - width (int): width of the rectangle
    - height (int): height of the rectangle
    - x (int): x-coordinate of the rectangle
    - y (int): y-coordinate of the rectangle
    - id (str): id of the rectangle

    Attributes:
    - width (int): width of the rectangle
    - height (int): height of the rectangle
    - x (int): x-coordinate of the rectangle
    - y (int): y-coordinate of the rectangle
    - id (str): id of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle object

        Args:
        - width (int): width of the rectangle
        - height (int): height of the rectangle
        - x (int): x-coordinate of the rectangle
        - y (int): y-coordinate of the rectangle
        - id (str): id of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height of the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x coord of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x coord of the rectangle
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y coord of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y coord of the rectangle
        """
        self.__y = value

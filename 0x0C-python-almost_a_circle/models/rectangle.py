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
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if int(width) <= 0:
            raise ValueError('width must be > 0')

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if int(height) <= 0:
            raise ValueError('height must be > 0')

        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if int(x) < 0:
            raise ValueError('x must be >= 0')

        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if int(y) < 0:
            raise ValueError('y must be >= 0')

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
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
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
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
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
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle to the console.
        The Rectangle is printed using the character "#".
        """
        [print("") for _ in range(0, self.__y)]
        for _ in range(0, self.__height):
            [print(" ", end="") for _ in range(0, self.__x)]
            [print("#", end="") for _ in range(0, self.__width)]
            print("")

    def __str__(self):
        """
        Str repr for the class
        """
        str_repr = "[Rectangle] "
        str_repr += f"({self.id}) {self.__x}/{self.__y}"
        str_repr += f" - {self.__width}/{self.__height}"
        return str_repr

    def update(self, *args, **kwargs):
        """
        Assigns a key/value argument to attributes
        If args exists and is not empty, kwargs is skipped
        Each key in kwargs represents an attribute to the instance
        """
        if len(args) > 0:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

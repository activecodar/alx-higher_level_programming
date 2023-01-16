#!/usr/bin/python3

"""
The `models` package contains the base class for other
classes to inherit from.
"""


class Base:
    """
    Base class for other classes to inherit from.
    """

    __nb_objects = 0
    """
    Class attribute to keep track of the number of objects created.
    """

    def __init__(self, id=None):
        """
        Class constructor. Initializes the id attribute of the object.

        :param id: The id of the object. If not provided,
                   it will be automatically assigned.
        :type id: int, optional
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

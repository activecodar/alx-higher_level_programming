#!/usr/bin/python3

"""
The `models` package contains the base class for other
classes to inherit from.
"""
import json


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

    def to_json_string(list_dictionaries):
        """
        Converts a lit of dictionaries to a json object
        Args:
            list_dictionaries: List of dictionaries
        Returns:
            json: Json representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save json to file
        """
        filename = f"{cls.__name__}.json"
        list_dicts = []
        if list_objs is not None:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert the json to a string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

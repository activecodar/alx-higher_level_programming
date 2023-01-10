#!/usr/bin/python3
"""
Module for student class
"""


class Student:
    """
    Student Class that defines a student by their:
    - first name
    - last name
    - age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize the Student class with
        - first name
        - last name
        - age

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs: list = None) -> dict:
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): list of attribute names,
                          which needs to be included in the dictionary,
                          defaults to None

        Returns:
            dict: dictionary containing the serializable
                  attributes of a given class instance
                  based on the list passed
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

#!/usr/bin/python3
"""module has func that adds attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """
    Add new attribute to an object if it's possible

    Parameters:
        obj (object): The object to which the new attribute will be added
        attr_name (str): The name of the new attribute
        attr_value (Any): The value of the new attribute
    Raises:
        TypeError:  If the object can't have new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)

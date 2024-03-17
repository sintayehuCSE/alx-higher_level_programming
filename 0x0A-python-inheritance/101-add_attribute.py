#!/usr/bin/python3
"""Define a function that add new_attribute to an object
   if possible.
"""


def add_attribute(obj, name, value):
    """Adds a new-attribute to an object if possible.
       Args:
          obj (any): The object to which we add a new-attribute
          name (str): The new-attribute of obj
          value (any): The value of the new-attribute
      Return:
         TypeError: If obj can't have new-attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.name = value

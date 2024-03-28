#!/usr/bin/python3
"""Defines a base class for this project."""
import json


class Base:
    """The base class of this project.

       This class will be the base of all other classes in this project.
       The goal of it is to manage id attribute in all future classes and
       to avoid duplicating the same code (by extension, same bugs).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string of its argument."""
        if not list_dictionaries:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file."""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if not list_objs:
                f.write(cls.to_json_string(None))
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return ([])
        else:
            return (json.loads(json_string))

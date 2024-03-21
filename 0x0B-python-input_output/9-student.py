#!/usr/bin/python3
"""Define a class for maniipulating its instances's dictionary
   representation as a JSON string.
"""


class Student():
    """Define a Student class."""
    def __init__(self, first_name, last_name, age):
        """Instantiate class instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary repreesentation of Student's instance."""
        return (self.__dict__)

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

    def to_json(self, attrs=None):
        """Retrieves dictionary repreesentation of Student's instance."""
        if not attrs:
            return (self.__dict__)
        else:
            _dict_ = {}
            for i in range(len(attrs)):
                if hasattr(self, attrs[i]):
                    _dict_[attrs[i]] = self.__dict__[attrs[i]]
            return (_dict_)

#!/usr/bin/python3
"""Define one class."""


class BaseGeometry:
    """The base geometry class."""
    def area(self):
        """Raise an Exception error."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value of an integer.
           Args:
               name (string): Name of the object.
               value (int): The integer
           Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than zero.
           Return:
                 Nothing.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif (value <= 0):
            raise ValueError(name + " must be greater than 0")

#!/usr/bin/python3
"""Define one class."""


class Rectangle:
    """Define the rectangle class."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the instance of a rectangle.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        Raises:
            TypeError: If width or height is not int object.
            ValueError: If width or height is less than zero.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property for width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property for the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter of a rectangle."""
        if not self.width or not self.height:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """The string representation of rectangle object."""
        if self.width and self.height:
            for i in range(self.height):
                [print(self.print_symbol, end="") for j in range(self.width)]
                if i != (self.height - 1):
                    print()
        else:
            return ("")
        return ("")

    def __repr__(self):
        """Return string representation of rectangle object that can be used
           by eval() method to recreate the instance.
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Deletes a Rectangle with zero reference to it."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares and returns the bigger rectangle based on their area value.
           Args:
                rect_1 (Rectangle): The first Rectangle instance.
                rect_2 (Rectangle): The second Rectangle instance.
           Raises:
                TypeError: If either instances are not Rectangle type.
           Return:
                The bigger instance or first instance if both have equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a Rectangle instance with both width and height
           equal to size.
           Args:
               cls (Rectangle): Class Rectangle.
               size (int): Width and height of the square rectangle.
        """
        return (cls(size, size))

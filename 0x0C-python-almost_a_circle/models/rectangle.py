#!/usr/bin/python3
"""Define a rectangle class."""


from models.base import Base


class Rectangle(Base):
    """The rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the instance of a rectangle.
           Args:
               Width (int): The width of the Rectangle.
               height (int): The height of the Recatangle.
               x (int): The x coordinate of the Rectangle.
               y (int): The y coordinate of the Rectangle.
           Raise:
               TypeError: If any of the arguments are not an exact integer.
               ValueError: (If heigh or width <= 0) and (x or y < 0)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of a rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of a rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Get the value of 'x' coordinate."""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Gets the value of a 'y' coordinate."""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Gets the area of a Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Print # character representation of a rectangle."""
        [print() for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for k in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print()

    def update(self, *args, **kwargs):
        """Updates the Rectangle instance with a tuple of argument.
           Args:
               self (Rectangle): The rectangle
               args (tuple): Tuple of non-keyworded argument
               kwargs (dictionary): Dictionary of key-worded argument
        """
        if not args:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == 'height':
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]
            return (1)
        for i in range(len(args)):
            if i == 5:
                break
            elif i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]

    def __str__(self):
        """Return nice-printable string representation of Rectangle object."""
        s1 = "[Rectangle] " + '(' + str(self.id) + ')' + " " + str(self.__x)
        s = "/" + str(self.__y) + " - " + str(self.__width) + "/"
        return (s1 + s + str(self.__height))

#!/usr/bin/python3
"""Defines a base class for this project."""
import json
import turtle


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
        """Return dictionary object from JSON string."""
        if not json_string:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return a dummy instance with all attributes set.
           Args:
              cls (class): The class of dummy instance
              dictionary (dict): Dictionary of dummy instance attribute.
           Return:
               O: if Unknown class name is encountered.
               dummy_obj (object): If class name exist and valid.
        """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_obj = cls(1)
        else:
            print("Unknown class name")
            return (0)
        dummy_obj.update(**dictionary)
        return (dummy_obj)

    @classmethod
    def load_from_file(cls):
        """Return a list of instance, having their attribute set to data
           from a file.
        """
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                jstr = f.read()
                list_dict = cls.from_json_string(jstr)
                list_obj = [cls.create(**item) for item in list_dict]
                return (list_obj)
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save CSV string of object to a file."""
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file_csv(cls):
        """Reconstruct python object from CSV file."""
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as f:
                jstr = f.read()
                list_dict = cls.from_json_string(jstr)
                obj_list = [cls.create(**attr) for attr in list_dict]
                return (obj_list)
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw a list of rectangles and Squares on Canvas.
           Args:
               list_rectangles (list): List of Rectangles instance.
               list_squares (list): List of Square instance
        """
        tur_obj = turtle.Turtle()
        tur_obj.shape("turtle")
        tur_obj.screen.bgcolor("#00adef")
        tur_obj.screen.title("Sintayehu Mulugeta Kebede")
        tur_obj.speed(3)
        tur_obj.pensize(5)
        tur_obj.pu()
        tur_obj.hideturtle()
        tur_obj.goto(-165, 290)
        tur_obj.pencolor("#ffffff")
        tur_obj.write("Cooperative Bank of Oromia", True, align="center", font=("Arial", 30, "normal"))


        tur_obj.penup()
        tur_obj.home()
        tur_obj.showturtle()
        tur_obj.pencolor("#000000")
        for rect in list_rectangles:
            tur_obj.goto(rect.x, rect.y)
            if not tur_obj.isdown():
                tur_obj.down()
            for i in range(2):
                tur_obj.fd(rect.width)
                tur_obj.left(90)
                tur_obj.fd(rect.height)
                tur_obj.lt(90)
            tur_obj.up()
        tur_obj.pencolor("#e38524")
        for sqr in list_squares:
            tur_obj.setpos(sqr.x, sqr.y)
            if not tur_obj.isdown():
                tur_obj.pendown()
            for i in range(2):
                tur_obj.forward(sqr.size)
                tur_obj.left(90)
                tur_obj.fd(sqr.size)
                tur_obj.lt(90)
            tur_obj.penup()
        tur_obj.reset()

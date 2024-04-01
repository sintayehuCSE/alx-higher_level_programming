#!/usr/bin/python3
"""A test file for `rectangle` module."""
import sys #for redirecting standard out-put stream to fake file object
import io #for creating fake file object pointing to in memory stream
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_RectangleInit(unittest.TestCase):
    """Test the initialization of rectangle instance."""
    def test_parent_instance(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_isNotParent_type(self):
        self.assertIsNot(type(Rectangle(1, 1)), Base)

    def test_obj_type(self):
        self.assertIs(type(Rectangle(1, 1)), Rectangle)

    def test_whois_my_parent(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_insufficient_argument_one(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_insufficient_argument_two(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_insufficient_argument_three(self):
        with self.assertRaises(TypeError):
            Rectangle(x=0, y=0, id=None)

    def test_private_width(self):
        rw = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            print(rw.__width)

    def test_private_height(self):
        rh = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            print(rh.__height)

    def test_private_x(self):
        rx = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            print(rx.__x)

    def test_private_y(self):
        ry = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            print(ry.__y)

    def test_instance_id(self):
        self.assertEqual(Rectangle(1, 1, id=12).id, 12)

    def test_getter_of_width(self):
        self.assertEqual(Rectangle(1, 1).width, 1)

    def test_getter_of_height(self):
        self.assertEqual(Rectangle(1, 1).height, 1)

    def test_getter_of_x(self):
        self.assertEqual(Rectangle(1, 1).x, 0)

    def test_getter_of_y(self):
        self.assertEqual(Rectangle(1, 1).y, 0)

    def test_setter_of_width(self):
        rws = Rectangle(1, 1)
        rws.width = 10
        self.assertEqual(rws.width, 10)

    def test_setter_of_height(self):
        rhs = Rectangle(1, 1)
        rhs.height = 10
        self.assertEqual(rhs.height, 10)

    def test_setter_of_x(self):
        rxs = Rectangle(1, 1)
        rxs.x = 10
        self.assertEqual(rxs.x, 10)

    def  test_setter_of_y(self):
        rys = Rectangle(1, 1)
        rys.y = 10
        self.assertEqual(rys.y, 10)

class Test_Rectangle_Width(unittest.TestCase):
    """Define various test-case for width of a Rectangle."""
    def test_bool_false_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rbf = Rectangle(False, 1)

    def test_bool_true_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rbt = Rectangle(True, 1)
    def test_None_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rn = Rectangle(None, 1)

    def test_complex_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rc = Rectangle(complex(5), 1)

    def test_float_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rf = Rectangle(3.14, 1)

    def test_float_InF_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rfi = Rectangle(float('inf'), 1)

    def test_float_NaN_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rfn = Rectangle(float('nan'), 1)

    def test_string_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rs = Rectangle("Sintayehu", 1)

    def test_tuple_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rt = Rectangle((1, 2), 1)

    def test_list_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rl = Rectangle([1, 2], 1)

    def test_dictionary_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rd = Rectangle({"one": 1, "two": 2}, 1)

    def test_set_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rs = Rectangle({1, 2}, 1)

    def test_memoryview_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rm = Rectangle(memoryview(b'Sintayehu'), 1)

    def test_byte_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rb = Rectangle(bytes("Sintayehu", encoding="utf-8"), 1)

    def test_bytearray_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rba = Rectangle(bytearray("Sintayehu", encoding="utf-8"), 1)

    def test_frozenset_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rf = Rectangle(frozenset({1, 2, 3}), 1)

    def test_range_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rr = Rectangle(range(9), 1)

    def test_zero_width(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rz = Rectangle(0, 1)

    def test_negative_width(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rne = Rectangle(-10, 1)


class Test_Rectangle_Height(unittest.TestCase):
    """Define various test-case for height of a Rectangle."""
    def test_bool_false_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rbf = Rectangle(1, False)

    def test_bool_true_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rbt = Rectangle(1, True)
    def test_None_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rn = Rectangle(1, None)

    def test_complex_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rc = Rectangle(1, complex(5))

    def test_float_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rf = Rectangle(1, 3.14)

    def test_float_InF_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rfi = Rectangle(1, float('inf'))

    def test_float_NaN_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rfn = Rectangle(1, float('nan'))

    def test_string_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rs = Rectangle(1, "Sintayehu")

    def test_tuple_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rt = Rectangle(1, (1, 2))

    def test_list_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rl = Rectangle(1, [1, 2])

    def test_dictionary_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rd = Rectangle(1, {"one": 1, "two": 2})

    def test_set_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rs = Rectangle(1, {1, 2})

    def test_memoryview_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rm = Rectangle(1, memoryview(b'Sintayehu'))

    def test_byte_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rb = Rectangle(bytes(1, "Sintayehu", encoding="utf-8"))

    def test_bytearray_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rba = Rectangle(1, bytearray("Sintayehu", encoding="utf-8"))

    def test_frozenset_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rf = Rectangle(1, frozenset({1, 2, 3}))

    def test_range_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rr = Rectangle(1, range(9))

    def test_zero_height(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            rz = Rectangle(1, 0)

    def test_negative_height(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            rne = Rectangle(1, -10)


class Test_Rectangle_X_Coordinate(unittest.TestCase):
    """Define various test-case for x-coordinate of a Rectangle."""
    def test_bool_false_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rbf = Rectangle(1, 1, False)

    def test_bool_true_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rbt = Rectangle(1, 1, True)
    def test_None_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rn = Rectangle(1, 1, None)

    def test_complex_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rc = Rectangle(1, 1, complex(5))

    def test_float_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rf = Rectangle(1, 1, 3.14)

    def test_float_InF_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rfi = Rectangle(1, 1, float('inf'))

    def test_float_NaN_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rfn = Rectangle(1, 1, float('nan'))

    def test_string_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rs = Rectangle(1, 1, "Sintayehu")

    def test_tuple_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rt = Rectangle(1, 1, (1, 2))

    def test_list_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rl = Rectangle(1, 1, [1, 2])

    def test_dictionary_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rd = Rectangle(1, 1, {"one": 1, "two": 2})

    def test_set_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rs = Rectangle(1, 1, {1, 2})

    def test_memoryview_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rm = Rectangle(1, 1, memoryview(b'Sintayehu'))

    def test_byte_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rb = Rectangle(bytes(1, 1, "Sintayehu", encoding="utf-8"))

    def test_bytearray_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rba = Rectangle(1, 1, bytearray("Sintayehu", encoding="utf-8"))

    def test_frozenset_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rf = Rectangle(1, 1, frozenset({1, 2, 3}))

    def test_range_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rr = Rectangle(1, 1, range(9))

    def test_zero_x(self):
        self.assertEqual(Rectangle(1,1).x, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            rne = Rectangle(1, 1, -10)


class Test_Rectangle_Y_Coordinate(unittest.TestCase):
    """Define various test-case for y-coordinate of a Rectangle."""
    def test_bool_false_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rbf = Rectangle(1, 1, 0, False)

    def test_bool_true_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rbt = Rectangle(1, 1, 0, True)
    def test_None_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rn = Rectangle(1, 1, 0, None)

    def test_complex_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rc = Rectangle(1, 1, 0, complex(5))

    def test_float_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rf = Rectangle(1, 1, 0, 3.14)

    def test_float_InF_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rfi = Rectangle(1, 1, 0, float('inf'))

    def test_float_NaN_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rfn = Rectangle(1, 1, 0, float('nan'))

    def test_string_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rs = Rectangle(1, 1, 0, "Sintayehu")

    def test_tuple_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rt = Rectangle(1, 1, 0, (1, 2))

    def test_list_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rl = Rectangle(1, 1, 0, [1, 2])

    def test_dictionary_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rd = Rectangle(1, 1, 0, {"one": 1, "two": 2})

    def test_set_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rs = Rectangle(1, 1, 0, {1, 2})

    def test_memoryview_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rm = Rectangle(1, 1, 0, memoryview(b'Sintayehu'))

    def test_byte_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rb = Rectangle(bytes(1, 1, 0, "Sintayehu", encoding="utf-8"))

    def test_bytearray_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rba = Rectangle(1, 1, 0, bytearray("Sintayehu", encoding="utf-8"))

    def test_frozenset_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rf = Rectangle(1, 1, 0, frozenset({1, 2, 3}))

    def test_range_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            rr = Rectangle(1, 1, 0, range(9))

    def test_zero_y(self):
        self.assertEqual(Rectangle(1,1).y, 0)

    def test_negative_y(self):
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            rne = Rectangle(1, 1, 0, -10)

class Test_Rectangle_Area(unittest.TestCase):
    """A unittest for the area() method of a rectangle."""
    def test_rectangle_area_small(self):
        ra = Rectangle(10, 2)
        self.assertEqual(ra.area(), 20)

    def test_rectangle_area_invalid(self):
        with self.assertRaises(TypeError):
            ri = Rectangle(1,1)
            print(ri.area(1))

    def test_rectangle_area_large(self):
        rl = Rectangle(999999999999999, 999999999999999999)
        self.assertEqual(999999999999998999000000000000001, rl.area())

    def test_rectangle_area_updated(self):
        ru = Rectangle(1, 1)
        ru.update(ru.id, 12, 2)
        self.assertEqual(ru.area(), 24)


class Test_Rectangle_stdout_method(unittest.TestCase):
    """Test the correctness of the __str__ magic method of Rectangle class."""
    @classmethod
    def clipboard_stdout(cls, rect_obj, meth=None):
        """Capture the content of a standard out-put stream.
           Args:
               cls (class): The class of this method.
               rect_obj (instance): The instance of Rectangle to be printed.
               meth (method): Method called on Rectangle instance.
          Return:
               Clipboard of standard out-put stream.
        """
        clip = io.StringIO()
        sys.stdout = clip

        if meth == "print" or meth == "str":
            print(rect_obj)
        else:
            rect_obj.display()

        sys.stdout = sys.__stdout__
        return (clip)
    # Test of the magic __str__ dendur method of Rectangle instance. #
    def test_str_method_width_height(self):
        rwh = Rectangle(1, 1)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rwh, "print")
        expected = "[Rectangle] ({}) 0/0 - 1/1\n".format(rwh.id)
        self.assertEqual(got.getvalue(), expected)
        got.close()

    def test_str_method_width_height_x(self):
        rwhx = Rectangle(1, 1, 10)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rwhx, "str")
        expected = "[Rectangle] ({}) 10/0 - 1/1\n".format(rwhx.id)
        self.assertEqual(got.getvalue(), expected)
        got.close()

    def test_str_method_width_height_x_y(self):
        rwhxy = Rectangle(1, 1, 10, 20)
        expected = "[Rectangle] ({}) 10/20 - 1/1".format(rwhxy.id)
        self.assertEqual(expected, rwhxy.__str__())

    def test_str_method_width_height_x_y_id(self):
        rwhxyi = Rectangle(1, 1, 10, 20, 120)
        expected = "[Rectangle] (120) 10/20 - 1/1"
        self.assertEqual(expected, str(rwhxyi))

    def test_direct_print(self):
        rdp = Rectangle(1, 1, 10, 20, 120)
        expected = None
        self.assertEqual(expected, print(rdp))

    def test_updated_print(self):
        rup = Rectangle(1, 1)
        rup.update(120, 30, 40, 10, 20)
        expected = "[Rectangle] (120) 10/20 - 30/40\n"
        got = Test_Rectangle_stdout_method.clipboard_stdout(rup, "print")
        self.assertEqual(got.getvalue(), expected)
        got.close()

    def test_changed_print(self):
        rcp = Rectangle(7, 7, 0, 0, 400)
        rcp.width = 30
        rcp.height = 40
        rcp.x = 10
        rcp.y = 20
        expected = "[Rectangle] ({}) 10/20 - 30/40\n".format(rcp.id)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rcp, "str")
        self.assertEqual(expected, got.getvalue())
        got.close()

    def test_invalid_call_to_dunder_str(self):
        with self.assertRaises(TypeError):
            ric = Rectangle(1, 1)
            ric.__str__(1)

    #Test of the display() method of Rectangle instance. #

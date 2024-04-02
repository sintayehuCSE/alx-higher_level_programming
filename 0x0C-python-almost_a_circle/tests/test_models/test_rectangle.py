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
    """Test the correctness of the __str__ magic method of Rectangle class.
       Plus the out-put of the display method of Rectangle class.
    """
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
    # Test of the magic __str__ method of Rectangle instance. #
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
    def test_display_width_height_one(self):
        rdwho = Rectangle(2, 2)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rdwho)
        expected = "##\n##\n"
        self.assertEqual(got.getvalue(), expected)
        got.close()

    def test_display_width_height_two(self):
        rdwht = Rectangle(4, 6)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rdwht, "display")
        expected = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(got.getvalue(), expected)
        got.close()

    def test_display_width_height_x(self):
        rdwhx = Rectangle(2, 2, 2)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rdwhx, "display")
        expected = "  ##\n  ##\n"
        self.assertEqual(got.getvalue(), expected)
        got.close()

    def test_display_width_height_three(self):
        rdwh3 = Rectangle(1, 1)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rdwh3)
        self.assertEqual("#\n", got.getvalue())
        got.close()

    def test_display_width_height_y(self):
        rdwhy = Rectangle(2, 2, y=2)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rdwhy)
        self.assertEqual("\n\n##\n##\n", got.getvalue())
        got.close()

    def test_display_width_height_x_y(self):
        rdwhxy = Rectangle(2, 2, 2, 2)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rdwhxy)
        expected = "\n\n  ##\n  ##\n"
        self.assertEqual(expected, got.getvalue())
        got.close()

    def test_updated_display(self):
        rud = Rectangle(1, 1)
        args = (rud.id, 3, 3, 2, 2)
        rud.update(*args)
        got = Test_Rectangle_stdout_method.clipboard_stdout(rud, "display")
        expected = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(expected, got.getvalue())
        got.close()

    def test_changed_display(self):
        rcd = Rectangle(1, 1)
        rcd.width = 3
        rcd.height = 3
        rcd.x = 2
        rcd.y = 2
        got = Test_Rectangle_stdout_method.clipboard_stdout(rcd, "display")
        expected = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(expected, got.getvalue())
        got.close()

    def test_invalid_call_to_display_method(self):
        with self.assertRaises(TypeError):
            rictdm = Rectangle(1, 1)
            rictdm.display(rictdm.id)


class Test_Rectangle_Update_Method(unittest.TestCase):
    """Test the correct operation of display() method of rectangle module."""
    #Test with unpacked and packed tuple of argument
    def test_update_wtup_no_argument(self):
        runa = Rectangle(1, 1)
        runa.update()
        expected = {'id': runa.id, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': runa.id, 'width': runa.width, 'height': runa.height, 'x':
               runa.x, 'y': runa.y}
        self.assertEqual(got, expected)

    def test_update_wtup_id(self):
        rui = Rectangle(1, 1)
        rui.update(578)
        expected = {'id': 578, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rui.id, 'width': rui.width, 'height': rui.height, 'x':
               rui.x, 'y': rui.y}
        self.assertEqual(got, expected)

    def test_update_wtup_id_width(self):
        ruiw = Rectangle(1, 1)
        ruiw.update(586, 10)
        expected = {'id': 586, 'width': 10, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': ruiw.id, 'width': ruiw.width, 'height': ruiw.height, 'x':
               ruiw.x, 'y': ruiw.y}
        self.assertEqual(got, expected)

    def test_update_wtup_id_width_height(self):
         ruiwh = Rectangle(1, 1)
         ruiwh.update(594, 10, 20)
         expected = {'id': 594, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
         got = {'id': ruiwh.id, 'width': ruiwh.width, 'height': ruiwh.height,
                'x':ruiwh.x, 'y': ruiwh.y}
         self.assertEqual(got, expected)

    def test_update_wtup_id_width_height_x(self):
        ruiwhx = Rectangle(1, 1)
        ruiwhx.update(602, 10, 20, 100)
        expected = {'id': 602, 'width': 10, 'height': 20, 'x': 100, 'y': 0}
        got = {'id': ruiwhx.id, 'width': ruiwhx.width, 'height': ruiwhx.height,'x':
               ruiwhx.x, 'y': ruiwhx.y}
        self.assertEqual(got, expected)

    def test_update_wtup_id_width_height_x_y(self):
        ruiwhxy = Rectangle(1, 1)
        ruiwhxy.update(610, 10, 20, 100, 200)
        expected = {'id': 610, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': ruiwhxy.id, 'width': ruiwhxy.width, 'height': ruiwhxy.height,
               'x':ruiwhxy.x, 'y': ruiwhxy.y}
        self.assertEqual(got, expected)

    def test_update_wtup_excess_tuple_argument(self):
        rueta = Rectangle(1, 1)
        rueta.update(618, 10, 20, 100, 200, 400, 800, 1000)
        expected = {'id': 618, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': rueta.id, 'width': rueta.width, 'height': rueta.height,
               'x':rueta.x, 'y': rueta.y}
        self.assertEqual(got, expected)

    def test_update_wtup_packed_empty(self):
        rupe = Rectangle(1, 1)
        args = ()
        rupe.update(*args)
        expected = {'id': rupe.id, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rupe.id, 'width': rupe.width, 'height': rupe.height, 'x':
               rupe.x, 'y': rupe.y}
        self.assertEqual(got, expected)

    def test_update_wtup_packed_id(self):
        rupi = Rectangle(1, 1)
        args = (635, )
        rupi.update(*args)
        expected = {'id': 635, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rupi.id, 'width': rupi.width, 'height': rupi.height, 'x':
               rupi.x, 'y': rupi.y}
        self.assertEqual(got, expected)

    def test_update_wtup_packed_id_width(self):
        rupiw = Rectangle(1, 1)
        args = (644, 10)
        rupiw.update(*args)
        expected = {'id': 644, 'width': 10, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rupiw.id, 'width': rupiw.width, 'height': rupiw.height, 'x':
               rupiw.x, 'y': rupiw.y}
        self.assertEqual(got, expected)

    def test_update_wtup_packed_id_width_height(self):
        rupiwh = Rectangle(1, 1)
        args = (658, 10, 20)
        rupiwh.update(*args)
        expected = {'id': 658, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        got = {'id': rupiwh.id, 'width': rupiwh.width, 'height': rupiwh.height,
                'x':rupiwh.x, 'y': rupiwh.y}
        self.assertEqual(got, expected)

    def test_update_wtup_packed_id_width_height_x(self):
        rupiwhx = Rectangle(1, 1)
        args = (667, 10, 20, 100)
        rupiwhx.update(*args)
        expected = {'id': 667, 'width': 10, 'height': 20, 'x': 100, 'y': 0}
        got = {'id': rupiwhx.id, 'width': rupiwhx.width, 'height': rupiwhx.height,'x':
               rupiwhx.x, 'y': rupiwhx.y}
        self.assertEqual(got, expected)

    def test_update_wtup_packed_id_width_height_x_y(self):
        rupiwhxy = Rectangle(1, 1)
        args = (676, 10, 20, 100, 200)
        rupiwhxy.update(*args)
        expected = {'id': 676, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': rupiwhxy.id, 'width': rupiwhxy.width, 'height': rupiwhxy.height,
               'x':rupiwhxy.x, 'y': rupiwhxy.y}
        self.assertEqual(got, expected)

    def test_update_wtup_packed_excess_tuple_argument(self):
        rupeta = Rectangle(1, 1)
        args = (685, 10, 20, 100, 200, 400, 800, 1000, 5000, 10000, 20000)
        rupeta.update(*args)
        expected = {'id': 685, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': rupeta.id, 'width': rupeta.width, 'height': rupeta.height,
               'x':rupeta.x, 'y': rupeta.y}
        self.assertEqual(got, expected)

    #Test with unpacked and packed key/value pairs of argument
    def test_update_wdict_empty(self):
        rude = Rectangle(1, 1)
        rude.update()
        expected = {'id': rude.id, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rude.id, 'width': rude.width, 'height': rude.height, 'x':
               rude.x, 'y': rude.y}
        self.assertEqual(got, expected)

    def test_update_wdict_id(self):
        rudi = Rectangle(1, 1)
        rudi.update(id=699)
        expected = {'id': 699, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rudi.id, 'width': rudi.width, 'height': rudi.height, 'x':
               rudi.x, 'y': rudi.y}
        self.assertEqual(got, expected)

    def test_update_wdict_id_width(self):
        rudiw = Rectangle(1,1)
        rudiw.update(id=711, width=10)
        expected = {'id': 711, 'width': 10, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rudiw.id, 'width': rudiw.width, 'height': rudiw.height, 'x':
               rudiw.x, 'y': rudiw.y}
        self.assertEqual(got, expected)

    def test_update_wdict_id_width_height(self):
        rudiwh = Rectangle(1, 1)
        rudiwh.update(id=719, width=10, height=20)
        expected = {'id': 719, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        got = {'id': rudiwh.id, 'width': rudiwh.width, 'height': rudiwh.height,
                'x':rudiwh.x, 'y': rudiwh.y}
        self.assertEqual(got, expected)

    def test_update_wdict_id_width_height_x(self):
        rudiwhx = Rectangle(1, 1)
        rudiwhx.update(id=727, width=10, height=20, x=100)
        expected = {'id': 727, 'width': 10, 'height': 20, 'x': 100, 'y': 0}
        got = {'id': rudiwhx.id, 'width': rudiwhx.width, 'height': rudiwhx.height,'x':
               rudiwhx.x, 'y': rudiwhx.y}
        self.assertEqual(got, expected)

    def test_update_wdict_id_width_height_x_y(self):
        rudiwhxy = Rectangle(1, 1)
        rudiwhxy.update(id=735, width=10, height=20, x=100, y=200)
        expected = {'id': 735, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': rudiwhxy.id, 'width': rudiwhxy.width, 'height': rudiwhxy.height,
               'x':rudiwhxy.x, 'y': rudiwhxy.y}
        self.assertEqual(got, expected)

    def test_update_wdict_excess_dict_argument(self):
        rudeta = Rectangle(1, 1)
        rudeta.update(id=743, width=10, height=20, x=100, y=200, age=27, gcpa=4, rank=1)
        expected = {'id': 743, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': rudeta.id, 'width': rudeta.width, 'height': rudeta.height,
               'x':rudeta.x, 'y': rudeta.y}
        self.assertEqual(got, expected)
    #Test with presence of packed keyworded argument
    def test_update_wdict_packed_empty(self):
        rupde = Rectangle(1, 1)
        kwargs = {}
        rupde.update(**kwargs)
        expected = {'id': rupde.id, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rupde.id, 'width': rupde.width, 'height': rupde.height, 'x':
               rupde.x, 'y': rupde.y}
        self.assertEqual(got, expected)

    def test_update_wdict_packed_id(self):
        rudpi = Rectangle(1, 1)
        kwargs = {'id': 760}
        rudpi.update(**kwargs)
        expected = {'id': 760, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rudpi.id, 'width': rudpi.width, 'height': rudpi.height, 'x':
               rudpi.x, 'y': rudpi.y}
        self.assertEqual(got, expected)

    def test_update_wdict_packed_id_width(self):
        rudpiw = Rectangle(1, 1)
        kwargs = {'id': 770, 'width': 10}
        rudpiw.update(**kwargs)
        expected = {'id': 770, 'width': 10, 'height': 1, 'x': 0, 'y': 0}
        got = {'id': rudpiw.id, 'width': rudpiw.width, 'height': rudpiw.height, 'x':
               rudpiw.x, 'y': rudpiw.y}
        self.assertEqual(got, expected)

    def test_update_wdict_packed_id_width_height(self):
        rudpiwh = Rectangle(1, 1)
        kwargs = {'id': 780, 'width': 10, 'height': 20}
        rudpiwh.update(**kwargs)
        expected = {'id': 780, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        got = {'id': rudpiwh.id, 'width': rudpiwh.width, 'height': rudpiwh.height, 'x':
               rudpiwh.x, 'y': rudpiwh.y}
        self.assertEqual(got, expected) 

    def test_update_wdict_packed_id_width_height_x(self):
        rudpiwhx = Rectangle(1, 1)
        kwargs = {'id': 790, 'width': 10, 'height': 20, 'x': 100}
        rudpiwhx.update(**kwargs)
        expected = {'id': 790, 'width': 10, 'height': 20, 'x': 100, 'y': 0}
        got = {'id': rudpiwhx.id, 'width': rudpiwhx.width, 'height': rudpiwhx.height, 'x':
               rudpiwhx.x, 'y': rudpiwhx.y}
        self.assertEqual(got, expected)           

    def test_update_wdict_packed_id_width_height_x_y(self):
        rudpiwhxy = Rectangle(1, 1)
        kwargs = {'id': 797, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        rudpiwhxy.update(**kwargs)
        expected = {'id': 797, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': rudpiwhxy.id, 'width': rudpiwhxy.width, 'height': rudpiwhxy.height, 'x':
               rudpiwhxy.x, 'y': rudpiwhxy.y}
        self.assertEqual(got, expected)

    def test_update_wdict_packed_excess_dict_argument(self):
        rudpeda = Rectangle(1, 1)
        kwargs = {'id': 800, 'width': 10, 'height': 20, 'x': 100, 'y': 200, 'age': 27, 'cgpa': 4, 'rank': 1}
        rudpeda.update(**kwargs)
        expected = {'id': 800, 'width': 10, 'height': 20, 'x': 100, 'y': 200}
        got = {'id': rudpeda.id, 'width': rudpeda.width, 'height': rudpeda.height, 'x':
               rudpeda.x, 'y': rudpeda.y}
        self.assertEqual(got, expected)
    #Tuple argument versus keyworded argument priority test, if both present
    def test_update_tup_or_dict_priority_one(self):
        rutodpo = Rectangle(1, 1)
        rutodpo.update(810, 10, 20, id=820, width=100, height=200, x=400, y=600)
        expected = {'id': 810, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        got = {'id': rutodpo.id, 'width': rutodpo.width, 'height': rutodpo.height, 'x':
               rutodpo.x, 'y': rutodpo.y}
        self.assertEqual(got, expected)

    def test_update_tup_or_dict_priority_two(self):
        rutodpt = Rectangle(1, 1)
        kwargs = {'id': 797, 'width': 1000, 'height': 2000, 'x': 100, 'y': 200}
        rutodpt.update(820, 10, 20, **kwargs)
        expected = {'id': 820, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        got = {'id': rutodpt.id, 'width': rutodpt.width, 'height': rutodpt.height, 'x':
               rutodpt.x, 'y': rutodpt.y}
        self.assertEqual(got, expected)

    def test_update_tup_or_dict_priority_three(self):
        rutodpth = Rectangle(1, 1)
        args = (830, 10, 20)
        rutodpth.update(*args, id=820, width=100, height=200, x=400, y=600)
        expected = {'id': 830, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        got = {'id': rutodpth.id, 'width': rutodpth.width, 'height': rutodpth.height, 'x':
               rutodpth.x, 'y': rutodpth.y}
        self.assertEqual(got, expected)

    def test_update_tup_or_dict_priority_four(self):
        rutodpf = Rectangle(1, 1)
        args = (840, 10, 20)
        kwargs = {'id': 797, 'width': 110, 'height': 210, 'x': 100, 'y': 200}
        rutodpf.update(*args, **kwargs)
        expected = {'id': 840, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        got = {'id': rutodpf.id, 'width': rutodpf.width, 'height': rutodpf.height, 'x':
               rutodpf.x, 'y': rutodpf.y}
        self.assertEqual(got, expected)
    #Test for checking invalid values of attribute during update operation.#
    def test_update_wtup_none_id(self):
        rutni = Rectangle(1, 1)
        rutni.update(None)
        expected = "[Rectangle] ({}) 0/0 - 1/1".format(rutni.id)
        self.assertEqual(expected, str(rutni))

    def test_update_wtup_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_wtup_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(89, "invalid")

    def test_update_wtup_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(89, 0)

    def test_update_wtup_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(89, -5)

    def test_update_wtup_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_wtup_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r.update(89, 1, 0)

    def test_update_wtup_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r.update(89, 1, -5)

    def test_update_wtup_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_wtup_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_wtup_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_wtup_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_wtup_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_wtup_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_wtup_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_wtup_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_wtup_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_wtup_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")

    def test_update_wdict_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_wdict_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_wdict_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_wdict_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(width="invalid")

    def test_update_wdict_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(width=0)

    def test_update_wdict_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(width=-5)

    def test_update_wdict_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(height="invalid")

    def test_update_wdict_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r.update(height=0)

    def test_update_wdict_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r.update(height=-5)

    def test_update_wdict_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(x="invalid")

    def test_update_wdict_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r.update(x=-5)

    def test_update_wdict_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r.update(y="invalid")

    def test_update_wdict_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r.update(y=-5)

    def test_update_wtup_and_wdict(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_wdict_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_wdict_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class Test_Rectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


class Test_Rectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")

if __name__ == "__main__":
    unittest.main() 
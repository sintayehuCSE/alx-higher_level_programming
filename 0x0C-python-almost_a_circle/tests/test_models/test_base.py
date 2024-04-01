#!/usr/bin/python3
"""Defines a unittest for base.py module.
"""
import unittest
from models.base import Base


class Test_BaseInit(unittest.TestCase):
    """Unitests for testing instantiation of the Base class."""
    def test_default_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_incremental_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_selected_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_none_id(self):
        self.assertEqual(Base(None).id, 3)

    def test_true_bool(self):
        self.assertTrue(Base(True).id)

    def test_false_bool(self):
        self.assertFalse(Base(False).id)

    def test_complex_id(self):
        self.assertEqual(Base(complex(5)).id, complex(5))

    def test_float_id(self):
        self.assertEqual(Base(3.14).id, 3.14)

    def test_string_id(self):
        self.assertEqual(Base("Sintayehu").id, "Sintayehu")

    def test_tuple_id(self):
        self.assertEqual(Base((1, 2, "Santa")).id, (1, 2, "Santa"))

    def test_list_id(self):
        self.assertEqual(Base([1, 2, 'Me']).id, [1, 2, 'Me'])

    def test_dictionary_id(self):
        self.assertEqual(Base({"One": 1, "Two": 2}).id, {"One": 1, "Two": 2})

    def test_set_id(self):
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_float_INF_id(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_float_NAN_id(self):
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_bytes_id(self):
        self.assertEqual(Base(b"Sintayehu").id, b"Sintayehu")

    def test_bytearray_id(self):
        self.assertEqual(Base(bytearray("Sintayehu", encoding="utf-8")).id, bytearray(b'Sintayehu'))

    def test_memorview_id(self):
        self.assertEqual(Base(memoryview(b"Santa")).id, memoryview(b"Santa"))

    def test_frozenset_id(self):
        self.assertEqual(Base(frozenset({1, 2, 3})).id, frozenset({1, 2, 3}))

    def test_range_id(self):
        self.assertEqual(Base(range(9)).id, range(9))

    def test_private_attr(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_instances)

    def test_private_base(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_instances)

    def test_over_argumented(self):
        with self.assertRaises(TypeError):
            Base(1, 2, 3, 4)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Defines a unittest for base.py module.
"""
import unittest
from models.base import Base


class TestBase_Instantiation(unittest.TestCase):
    """Unitests for testing instantiation of the Base class."""
    def test_one(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_two(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)


if __name__ == "__main__":
    unittest.main()

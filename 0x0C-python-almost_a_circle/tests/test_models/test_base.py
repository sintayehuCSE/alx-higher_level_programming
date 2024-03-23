#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test case build."""
    def test_one(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_two(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)
    def test_three(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
if __name__ == "__main__":
    unittest.main()

























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































#!/usr/bin/python3
"""This is a module that describe different test cases for
   'max_integer([...])' function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """SetUp a unitesting class for the specified method."""

    def testOrderedList(self):
        """Test for ordered element of list."""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def testUnorderedList(self):
        """Test for mixed element of a integer list."""
        unordered = [2, 3, 4, 7, 6]
        self.assertEqual(max_integer(unordered), 7)

    def testMaxBegin(self):
        """Test with max element at beginning."""
        max_begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_begin), 4)

    def testEmptyList(self):
        """Test for empty list as argument to the function."""
        self.assertEqual(max_integer, None)

    def testOneElementList(self):
        """Test case for list with one element."""
        one_elm_list = [27]
        self.assertEqual(max_integer(one_elm_list), 27)

    def test_list_with_floats_elem(self):
        """Test for max of float element in a list."""
        float_list = [2.56, 45.2, 25.12, 88.5]
        self.assertEqual(max_integer(float_list), 88.5)

    def test_mixed_list(self):
        """Test case for elements with varied type - int/float."""
        mixed = [4.5, 5.6, 10, 56]
        self.assertEqual(max_integer(mixed), 56)

    def test_negative_integers(self):
        """Test case for all negative element of a list."""
        negative = [-10, -56, -12, -52]
        self.assertEqual(max_integer(negative), -10)

    def test_string_element(self):
        """Test case for when the value of argument is string."""
        arg = "Sintayehu"
        self.assertEqual(max_integer(arg), 'y')

    def test_list_of_string_element(self):
        """Test case for when all element of the list ar str type."""
        arg_list = ['Sintayehu', 'Mulugeta', 'Kebede']
        self.assertEqual(max_integer(arg_list), 'Sintayehu')

    def test_empty_str_arg(self):
        """Test case fo when a string argument is empty."""
        str_arg = ""
        self.assertEqual(max_integer(str_arg), None)


if __name__ == "__main__":
    unittest.main()

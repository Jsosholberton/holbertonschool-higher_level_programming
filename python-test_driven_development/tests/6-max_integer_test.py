#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing the max integer from unittest"""

    def test_max_integer(self):
        """ a method with different cases """

        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([-99, -65, -6, -1, -9]), -1)
        self.assertEqual(max_integer([-1, -2, 65, 9, 99]), 99)
        self.assertEqual(max_integer([[6], [8], [1], [0]]), [8])
        self.assertEqual(max_integer([1.35, 4.9, 0.99, 15.8]), 15.8)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer(), None)

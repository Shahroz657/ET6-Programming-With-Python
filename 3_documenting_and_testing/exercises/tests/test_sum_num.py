#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 19 12 24

@author: Muhammad Shahroz
"""
import unittest

# --- imports & test class before documenting and testing ---

# from ..sum_num import sum_num

# class TestSumNum(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..sum_num import sum_num  # Import the function to test


class TestSumNum(unittest.TestCase):
    """Unit tests for the sum_num function"""

    def test_positive_numbers(self):
        """It should return the correct sum of two positive numbers"""
        self.assertEqual(sum_num(3, 5), 8)

    def test_negative_numbers(self):
        """It should return the correct sum of two negative numbers"""
        self.assertEqual(sum_num(-3, -2), -5)

    def test_mixed_numbers(self):
        """It should return the correct sum of a positive and a negative number"""
        self.assertEqual(sum_num(3, -2), 1)

    def test_zero(self):
        """It should return 0 if both arguments are 0"""
        self.assertEqual(sum_num(0, 0), 0)

    def test_large_numbers(self):
        """It should return the correct sum of two large numbers"""
        self.assertEqual(sum_num(1000000, 2000000), 3000000)

    def test_invalid_input(self):
        """It should raise a TypeError if arguments are not integers"""
        with self.assertRaises(TypeError):
            sum_num("3", 5)
        with self.assertRaises(TypeError):
            sum_num(3.5, 2)
        with self.assertRaises(TypeError):
            sum_num(None, 1)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    "hello"
    def test_one_element(self):
        "hello"
        v1 = [76]
        self.assertEqual(max_integer(v1), 76)

    def test_one_element(self):
        "hello"
        v1 = [76, 13, 15]
        self.assertEqual(max_integer(v1), 76)

#!/usr/bin/env python3
"""
test_utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestedAccessNestedMap(unittest.TestCase):
    """
    test nested access map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, input1, input2, answer):
        self.assertEqual(access_nested_map(input1, input2), answer)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, input1, input2, answer):
        with self.assertRaises(answer):
            access_nested_map(input1, input2)

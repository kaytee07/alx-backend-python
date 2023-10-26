#!/usr/bin/env python3
"""
test_utils module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Dict, Union, Tuple, Exception, Response


class TestedAccessNestedMap(unittest.TestCase):
    """
    test nested access map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, input1: Dict,
            input2: Tuple[str],
            answer: Union[Dict, int]
    ) -> None:
        self.assertEqual(access_nested_map(input1, input2), answer)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            input1: Dict,
            input2:Dict,
            answer: Exception
    ) -> None:
        with self.assertRaises(answer):
            access_nested_map(input1, input2)


class TestGetJson(unittest.TestCase):
    """
    test utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            mock_requests: Response
    ) -> None:
        """
        test utils.get_json
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests.get.return_value = mock_response
        result = get_json(test_url)
        mock_requests.get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

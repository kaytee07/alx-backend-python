#!/usr/bin/env python3
"""
test client.py
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    test all client functions
    """
    @parameterized.expand([
        ("google", {"github": "google"}),
        ("abc", {"github": "abx"})
    ])
    @patch("client.get_json")
    def test_org(self, organization: str, response: Dict, mock_get_json) -> None:
        """
        test that GithubOrgClient.org returns correct value
        """
        githuborgclient_instance = GithubOrgClient(organization)
        mock_get_json.return_value = response
        result = githuborgclient_instance.org
        self.assertEqual(result, response)
        mock_get_json.assert_called_once()

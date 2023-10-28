#!/usr/bin/env python3
"""
test client.py
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self):
        """
        test that  GithubOrgClient._public_repos_url
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

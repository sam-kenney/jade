"""Test the config module."""
from __future__ import annotations

import io
from unittest import mock

from jade.config import get_config


def test_get_config_no_file():
    """Test the get_config function."""
    assert get_config() == {"site": {"name": "My Site"}}


@mock.patch("jade.config.open")
def test_get_config_file(mock_open: mock.Mock):
    """Test the get_config function."""
    mock_open.return_value.__enter__.return_value.read.return_value = io.StringIO(
        "site:\n  name: My Site",
    )
    assert get_config() == {"site": {"name": "My Site"}}

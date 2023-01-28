"""Test the path module."""
from __future__ import annotations

import pathlib

import jade.path as path


def test_path_exists():
    """Test the path.exists function."""
    assert path.exists("tests")
    assert not path.exists("tests/does_not_exist")


def test_path_path():
    """Test the path.path function."""
    assert path.path("tests") == pathlib.Path("tests").expanduser().resolve()
    assert (
        path.path("tests/does_not_exist")
        == pathlib.Path("tests/does_not_exist").expanduser().resolve()
    )

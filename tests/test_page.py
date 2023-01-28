"""Test the page module."""
from __future__ import annotations

import textwrap
from unittest import mock

import pytest

from jade.page import Page


def test_from_markdown_no_frontmatter():
    """Test the from_markdown function."""
    page = Page.from_markdown("# Hello World")

    assert page.content == "# Hello World"
    assert page.frontmatter == {}


def test_from_markdown_with_frontmatter():
    """Test the from_markdown function."""
    page = Page.from_markdown(
        textwrap.dedent(
            """
            ---
            foo: bar
            ---
            # Hello World
            """,
        ),
    )

    assert page.content == "\n# Hello World\n"
    assert page.frontmatter == {"foo": "bar"}
    assert page.foo == "bar"


def test_open_content_raises_file_not_found():
    """Test the open_content function."""
    page = Page.from_markdown("# Hello World")

    with pytest.raises(FileNotFoundError):
        page.open_content("foo.md")


@mock.patch("jade.page.open")
def test_open_content_returns_file(mock_open):
    """Test the open_content function."""
    mock_open.return_value.__enter__.return_value.read.return_value = "Hello World"

    assert Page.open_content("") == "Hello World"


@mock.patch("jade.page.path.exists")
@mock.patch("jade.page.open")
def test_from_path(mock_open, mock_exists):
    """Test the from_path function."""
    mock_exists.return_value = True
    mock_open.return_value.__enter__.return_value.read.return_value = "Hello World"

    page = Page.from_path("")

    assert page.content == "Hello World"
    assert page.frontmatter == {}


def test_repr():
    """Test the __repr__ function."""
    page = Page.from_markdown("# Hello World")

    assert repr(page) == "Page({}, # Hello World)"


def test_render_content():
    """Test the render_content function."""
    page = Page.from_markdown("# Hello {{name}}")

    assert page.render_content(name="World") == "<h1>Hello World</h1>"

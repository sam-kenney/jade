"""Test the builder module."""
from __future__ import annotations

import pathlib

import jade.builder
from jade.page import Page


def test_build_url():
    """Test the _build_url function."""
    page = Page({}, "Some content")
    file = pathlib.Path("content/home.md")
    assert jade.builder._build_url(page, file) == "/home"

    page = Page({"permalink": "home"}, "Some content")
    assert jade.builder._build_url(page, file) == "/home"

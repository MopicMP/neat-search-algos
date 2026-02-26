"""Tests for neat-search-algos."""

import pytest
from neat_search_algos import algos


class TestAlgos:
    """Test suite for algos."""

    def test_basic(self):
        """Test basic usage."""
        result = algos("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            algos("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = algos(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities

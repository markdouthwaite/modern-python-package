"""Unit tests for the dummy module."""

from python_pkg import dummy_fn


def test_dummy_fn_returns_zero():
    """Assert that the dummy function returns the correct value"""

    assert dummy_fn() == 0

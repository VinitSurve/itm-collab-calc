"""Unit tests for calculator module."""

from calculator import add, subtract


def test_add_integers():
    assert add(10, 5) == 15


def test_add_negative_and_float():
    assert add(-3, 7.5) == 4.5


def test_subtract_integers():
    assert subtract(10, 4) == 6


def test_subtract_negative():
    assert subtract(3, 9) == -6

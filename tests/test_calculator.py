"""Unit tests for calculator module."""

import pytest
from calculator import add, subtract


def test_add_integers() -> None:
    assert add(10, 5) == 15


def test_add_negative_and_float() -> None:
    assert add(-3, 7.5) == 4.5


def test_subtract_integers() -> None:
    assert subtract(10, 4) == 6


def test_subtract_negative() -> None:
    assert subtract(3, 9) == -6


def test_rejects_boolean_operands() -> None:
    with pytest.raises(TypeError):
        add(True, 2)


def test_rejects_non_numeric_operands() -> None:
    with pytest.raises(TypeError):
        subtract("10", 5)  # type: ignore[arg-type]

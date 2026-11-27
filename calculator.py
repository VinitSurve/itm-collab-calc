"""Modular calculator module for Git collaboration practical."""

from typing import Union

Number = Union[int, float]


def _validate_operands(a: Number, b: Number) -> None:
    """Ensure operands are int or float and reject booleans."""
    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"Expected numeric operand, got {type(value).__name__}")


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numeric operands."""
    _validate_operands(a, b)
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference between two numeric operands (a - b)."""
    _validate_operands(a, b)
    return a - b

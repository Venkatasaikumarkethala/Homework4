"""
Unit tests for calculator module.
"""

import pytest
from calculator.calculator import add, subtract, multiply, divide

def test_add():
    """Tests the addition function."""
    assert add(2, 3) == 5

def test_subtract():
    """Tests the subtraction function."""
    assert subtract(5, 3) == 2

def test_multiply():
    """Tests the multiplication function."""
    assert multiply(4, 3) == 12

def test_divide():
    """Tests the division function."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Tests division by zero, expecting a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)

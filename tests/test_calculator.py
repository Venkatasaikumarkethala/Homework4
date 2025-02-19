import pytest
from calculator.calculator import add, subtract, multiply, divide

def test_add():
    """Test addition function"""
    assert add(2, 3) == 5

def test_subtract():
    """Test subtraction function"""
    assert subtract(10, 3) == 7

def test_multiply():
    """Test multiplication function"""
    assert multiply(4, 5) == 20

def test_divide():
    """Test division function"""
    assert divide(20, 4) == 5

def test_divide_by_zero():
    """Test division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1, 0)

import pytest
from calculator.calculator import Calculator

def test_operations_with_generated_data(generated_data):
    """Tests arithmetic operations with dynamically generated data."""
    for num1, num2, operation, expected in generated_data:
        if expected == "ZeroDivisionError":
            with pytest.raises(ZeroDivisionError):
                Calculator.perform_operation(num1, num2, operation)
        else:
            result = Calculator.perform_operation(num1, num2, operation)
            assert result == expected, f"Expected {expected}, but got {result}"
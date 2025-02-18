"""
Calculator module for basic arithmetic operations.
"""

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference between two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of two numbers. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

class Calculator:
    """Handles arithmetic operations using static methods."""

    @staticmethod
    def perform_operation(num1: float, num2: float, operation):
        """Executes the given arithmetic operation."""
        if operation not in [add, subtract, multiply, divide]:
            raise ValueError("Invalid operation")
        
        return operation(num1, num2)
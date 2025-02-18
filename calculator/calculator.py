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
    """Simple calculator class that supports basic operations."""
    
    @staticmethod
    def perform_operation(num1, num2, operation):
        """Executes the given arithmetic operation based on string input."""
        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
        }

        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")

        return operations[operation](num1, num2)
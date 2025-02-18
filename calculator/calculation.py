"""
Module containing the Calculation class for arithmetic operations.
"""

from typing import Callable

class Calculation:
    """Encapsulates an arithmetic operation with operands and a function."""
    
    def __init__(self, number1: float, number2: float, operation: Callable[[float, float], float]):
        """Initialize a Calculation with two numbers and an operation."""
        self.number1 = number1
        self.number2 = number2
        self.operation = operation
        self.result = self.operation(number1, number2)

    def get_result(self) -> float:
        """Returns the result of the calculation."""
        return self.result

"""
Module to store and manage a history of calculations.
"""

from typing import List, Type
from calculator.calculation import Calculation  # Ensure you're importing the class, NOT the module

class Calculations:
    """Manages a history of Calculation instances."""
    
    history: List[Type[Calculation]] = []  # Correctly reference the Calculation class

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a calculation to history."""
        cls.history.append(calculation)

    @classmethod
    def get_latest(cls) -> Calculation:
        """Retrieves the most recent calculation."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_all_calculations(cls) -> List[Calculation]:
        """Returns all stored calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears the entire calculation history."""
        cls.history.clear()

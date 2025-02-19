import sys
from decimal import Decimal, InvalidOperation
from calculator.calculator import Calculator  # Ensure correct import path

def calculate_and_print(a, b, operation):
    """
    Handles arithmetic calculations with error handling.

    Args:
        a (str): First number as a string.
        b (str): Second number as a string.
        operation (str): Arithmetic operation ("add", "subtract", "multiply", "divide").

    Returns:
        Prints the calculation result or an error message.
    """
    try:
        # Convert inputs to Decimal for accuracy
        a_decimal, b_decimal = Decimal(a), Decimal(b)
        
        # Perform the operation using Calculator class
        result = Calculator.perform_operation(a_decimal, b_decimal, operation)
        
        print(f"The result of {a} {operation} {b} is equal to {result}")
    
    except InvalidOperation:
        print(f"Invalid number input: '{a}' or '{b}' is not a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Entry point for command-line execution.
    Usage: python main.py <number1> <number2> <operation>
    """
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv  # Extract arguments
    calculate_and_print(a, b, operation)

if __name__ == "__main__":
    main()
from calculator.calculator import Calculator


def test_operations_with_generated_data(generated_data):
    """
    Tests arithmetic operations with dynamically generated data.
    Uses Faker-generated values for a, b, operation, and expected result.
    """
    for num1, num2, operation, expected in generated_data:
        try:
            result = Calculator.perform_operation(num1, num2, operation)
            assert result == expected
        except ZeroDivisionError:
            assert expected == "ZeroDivisionError"
        except ValueError as err:
            assert str(err) == f"Invalid operation: {operation}"

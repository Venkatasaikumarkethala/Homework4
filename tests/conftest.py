import pytest
from decimal import Decimal
from faker import Faker
from calculator.calculator import add, subtract, multiply, divide, Calculator

fake = Faker()

def generate_test_data(num_records):
    """Generate test data using Faker for arithmetic operations."""
    operation_mappings = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))

        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # ✅ Ensure b is never zero for division
        if operation_name == "divide":
            b = Decimal(fake.random_int(min=1, max=99))  # Ensures b is always at least 1

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"  # Handles division by zero errors

        yield a, b, operation_name, expected

@pytest.fixture
def generated_data(request):
    """Fixture to generate test data dynamically for tests."""
    num_records = request.config.getoption("--num_records")
    return list(generate_test_data(num_records))

def pytest_addoption(parser):
    """Adds the `--num_records` command-line option for pytest."""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")
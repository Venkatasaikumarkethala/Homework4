from decimal import Decimal  # Standard library import
import pytest  # Third-party import
from faker import Faker
from calculator.calculator import add, subtract, multiply, divide

fake = Faker()


@pytest.fixture
def generated_data(request):
    """Generate test data using Faker for arithmetic operations."""
    num_records = request.config.getoption("--num_records")

    operation_mappings = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    data = []
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = (
            Decimal(fake.random_number(digits=2))
            if _ % 4 != 3
            else Decimal(fake.random_number(digits=1))
        )
        operation_name = fake.random_element(
            elements=list(operation_mappings.keys())
        )

        # Ensure b is not zero for divide operation
        if operation_name == "divide" and b == 0:
            b = Decimal("1")

        try:
            expected = operation_mappings[operation_name](a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        data.append((a, b, operation_name, expected))

    return data


def pytest_addoption(parser):
    """
    Adds the `--num_records` command-line option for pytest.
    This allows users to specify how many test cases they want to generate dynamically.
    """
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

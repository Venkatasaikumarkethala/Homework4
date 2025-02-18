from faker import Faker
import random

fake = Faker()

def test_fake_calculations():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(["add", "subtract", "multiply", "divide"])
    
    print(f"Testing {operation} on {num1} and {num2}")

test_fake_calculations()
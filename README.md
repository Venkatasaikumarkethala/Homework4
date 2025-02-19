Hello this is my Homework 4

.# 📌 Advanced Calculator

This is the Advanced Calculator implementation for Homework 4. It extends the Basic Calculator from Homework 3 by adding:

Faker Library for Dynamic Test Data Generation
Automated Test Case Generation with pytest --num_records=N
Command-Line Interface (CLI) for User Input
Exception Handling for Robust Error Prevention
Pylint & Coverage for Code Quality Assurance
---

## 📜 Features

✅ Basic Arithmetic Operations (Add, Subtract, Multiply, Divide)
✅ OOP-Based Calculator Implementation (Static Methods, Instance Methods, Class Methods)
✅ Calculation History Storage & Retrieval
✅ Faker Integration for generating random test data
✅ Dynamic Test Case Generation with pytest --num_records=100
✅ Exception Handling (e.g., Divide by Zero, Invalid Inputs)
✅ Command-Line Interface (CLI) for direct user input
✅ 100% Test Coverage, Pylint, and Code Quality Checks

---

## 📂 Project Structure

homework4_project/
│── calculator/
│   │── __init__.py
│   │── calculator.py    # Implements the calculator logic
│   │── calculations.py  # Manages calculation history
│   │── calculation.py   # Defines a Calculation object
│── tests/
│   │── test_calculator.py   # Unit tests for calculator operations
│   │── test_faker.py        # Tests using Faker-generated data
│   │── conftest.py          # Pytest fixture for test data generation
│── requirements.txt
│── .pylintrc
│── README.md
│── pytest.ini
│── main.py                 # Command-line interface for user input
│── .gitignore
---

## ⚙️ Installation & Setup

Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Venkatasaikumarkethala/Homework4.git
cd homework4_project
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the Calculator

### Using Python

You can directly import the calculator module and use it in Python:

```python
from calculator.calculator import Calculator

result = Calculator.perform_operation(10, 5, "add")
print(result)  # Output: 15

Using the Command-Line Interface (CLI)

## 🛠️ Running Tests

### Run Pytest
``Bash``

python main.py 5 3 add
python main.py 10 2 subtract
python main.py 4 5 multiply
python main.py 20 4 divide

Expected Output
The result of 5 add 3 is equal to 8
The result of 10 subtract 2 is equal to 8
The result of 4 multiply 5 is equal to 20
The result of 20 divide 4 is equal to 5

Handling Errors
python main.py 1 0 divide  # Error: Cannot divide by zero
python main.py 5 b add  # Error: Invalid number input
python main.py 10 2 mod  # Error: Unknown operation

pytest tests/
```

✔️ If all tests pass, you’ll see an output like:

```
========================== 6 passed in 0.06s ==========================
```

### Run Pytest with Faker-Generated Data

```bash
pytest --num_records=10
```
Run Coverage Report
```bash
pytest --cov
```
---

## 📜 Code Explanation

###  Calculator Operations (calculator.py)
	•	perform_operation(num1, num2, operation): Executes an arithmetic operation.
	•	get_history(): Retrieves all past calculations.
	•	clear_history(): Clears stored calculations.

🔹 Calculation History (calculations.py)
	•	Stores previous calculations.
	•	Implements class methods to retrieve and clear history.

🔹 Dynamic Test Data (test_faker.py)
	•	Uses Faker to generate random numbers & operations.
	•	Tests multiple cases dynamically.

🔹 Command-Line Interface (main.py)
	•	Accepts user input (a, b, operation) and runs calculations.
	•	Implements error handling for invalid inputs.

----
🎯 Example Test Cases (Professor’s Instructions)

✔️ "5", "3", 'add' → "The result of 5 add 3 is equal to 8"
✔️ "10", "2", 'subtract' → "The result of 10 subtract 2 is equal to 8"
✔️ "4", "5", 'multiply' → "The result of 4 multiply 5 is equal to 20"
✔️ "20", "4", 'divide' → "The result of 20 divide 4 is equal to 5"
✔️ "1", "0", 'divide' → "An error occurred: Cannot divide by zero"
✔️ "9", "3", 'unknown' → "Unknown operation: unknown"
✔️ "a", "3", 'add' → "Invalid number input: a or 3 is not a valid number."
✔️ "5", "b", 'subtract' → "Invalid number input: 5 or b is not a valid number."
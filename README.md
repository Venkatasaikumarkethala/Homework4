Hello this is my Homework 3

.# 📌 Basic Calculator - Level 1

This is the **Level 1 Basic Calculator** implementation for the assignment. It includes **four basic arithmetic operations**: **Addition, Subtraction, Multiplication, and Division**, along with **unit tests** to verify correctness.

---

## 📜 Features

✔️ Perform **Addition (+)**  
✔️ Perform **Subtraction (-)**  
✔️ Perform **Multiplication (×)**  
✔️ Perform **Division (÷) with Exception Handling** (division by zero raises an error)  
✔️ Unit tests using **pytest**  
✔️ Code style checked with **pylint**  
✔️ Project structure follows **Separation of Concerns**  

---

## 📂 Project Structure

```
calculator_project/
│── calculator/
│   │── __init__.py
│   │── calculator.py   # Basic arithmetic operations
│── tests/
│   │── test_calculator.py   # Unit tests
│── requirements.txt
│── .pylintrc
│── README.md
│── pytest.ini
│── .gitignore
```

---

## ⚙️ Installation & Setup

Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Venkatasaikumarkethala/Homework3.git
cd calculator_project
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
from calculator.calculator import add, subtract, multiply, divide

print(add(5, 3))          # Output: 8
print(subtract(10, 4))    # Output: 6
print(multiply(6, 7))     # Output: 42
print(divide(15, 3))      # Output: 5.0
```

---

## 🛠️ Running Tests

### Run Pytest

```bash
pytest tests/
```

✔️ If all tests pass, you’ll see an output like:

```
========================== 5 passed in 0.06s ==========================
```

### Run Pylint for Code Quality Check

```bash
pylint calculator/
```

---

## 📜 Code Explanation

### Basic Arithmetic Functions

- **`add(a, b)`:** Returns the sum of `a` and `b`.
- **`subtract(a, b)`:** Returns the difference of `a` and `b`.
- **`multiply(a, b)`:** Returns the product of `a` and `b`.
- **`divide(a, b)`:** Returns the quotient of `a` and `b`. Raises `ValueError` if `b == 0`.


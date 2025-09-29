# DevOps Pipeline Demo

This repository demonstrates a complete DevOps CI/CD pipeline with a simple Python calculator application and comprehensive unit tests.

## 🚀 Features

- **Simple Calculator Application**: Basic arithmetic operations (add, subtract, multiply, divide, power, even check)
- **Comprehensive Unit Tests**: 19 test cases covering all functionality including edge cases
- **GitHub Actions CI/CD Pipeline**: Automated testing, building, and deployment
- **Multi-Python Version Support**: Tests run on Python 3.8, 3.9, 3.10, and 3.11
- **Code Quality**: Integrated linting with flake8

## 📁 Project Structure

```
DevOps_Pineline/
├── calculator.py           # Main calculator application
├── test_calculator.py      # Unit tests for calculator
├── requirements.txt        # Python dependencies
├── .github/workflows/      # GitHub Actions CI/CD configuration
│   └── ci-cd.yml          # Main workflow file
└── README.md              # This file
```

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.8 or higher

### Running the Application
```bash
# Clone the repository
git clone https://github.com/DannisNguyen12/DevOps_Pineline.git
cd DevOps_Pineline

# Run the calculator demo
python calculator.py
```

### Running Tests
```bash
# Run all tests with verbose output
python test_calculator.py

# Or using unittest module
python -m unittest test_calculator.py -v
```

## 🧮 Calculator API

The `Calculator` class provides the following methods:

- `add(a, b)` - Addition
- `subtract(a, b)` - Subtraction  
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division (raises ValueError for division by zero)
- `power(base, exponent)` - Exponentiation
- `is_even(number)` - Check if number is even

### Example Usage
```python
from calculator import Calculator

calc = Calculator()
result = calc.add(10, 5)        # Returns 15
result = calc.divide(10, 2)     # Returns 5.0
result = calc.power(2, 3)       # Returns 8
result = calc.is_even(4)        # Returns True
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow includes:

### 1. **Test Stage**
- Runs on multiple Python versions (3.8, 3.9, 3.10, 3.11)
- Installs dependencies
- Performs code linting with flake8
- Runs comprehensive unit tests
- Executes application demo

### 2. **Build Stage**
- Creates distribution package
- Uploads build artifacts
- Only runs on main branch after successful tests

### 3. **Deploy Stage**
- Downloads build artifacts
- Simulates application deployment
- Only runs on main branch after successful build

### Workflow Triggers
- **Push** to `main` or `develop` branches
- **Pull requests** to `main` branch

## 🧪 Test Coverage

The test suite includes:

- **Unit Tests**: 17 individual test methods
- **Integration Tests**: 2 complex calculation tests
- **Edge Cases**: Division by zero, negative numbers, zero operations
- **Error Handling**: Proper exception testing

### Test Categories
- Addition tests (positive, negative, zero)
- Subtraction tests (various scenarios)
- Multiplication tests (including zero and negatives)
- Division tests (including zero division handling)
- Power operation tests
- Even number checking tests
- Integration tests for complex calculations

## 📊 Pipeline Status

[![DevOps Pipeline CI/CD](https://github.com/DannisNguyen12/DevOps_Pineline/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/DannisNguyen12/DevOps_Pineline/actions/workflows/ci-cd.yml)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run tests to ensure they pass: `python test_calculator.py`
5. Commit your changes: `git commit -m "Add feature"`
6. Push to your branch: `git push origin feature-name`
7. Create a Pull Request

## 📝 License

This project is created for educational purposes to demonstrate DevOps CI/CD pipeline concepts.

## 🎯 Learning Objectives

This repository demonstrates:
- Test-driven development (TDD)
- Continuous Integration (CI)
- Continuous Deployment (CD)
- Automated testing
- Code quality assurance
- Multi-environment testing
- Artifact management
- GitHub Actions workflows

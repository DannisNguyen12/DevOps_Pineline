"""
Simple Calculator Module for DevOps Pipeline Demo
This module provides basic arithmetic operations.
"""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        return base ** exponent
    
    def is_even(self, number):
        """Check if a number is even."""
        return number % 2 == 0


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("DevOps Pipeline Calculator Demo")
    print("=" * 30)
    
    # Demo calculations
    print(f"Addition: 10 + 5 = {calc.add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {calc.subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {calc.multiply(10, 5)}")
    print(f"Division: 10 / 5 = {calc.divide(10, 5)}")
    print(f"Power: 2^3 = {calc.power(2, 3)}")
    print(f"Is 10 even? {calc.is_even(10)}")
    print(f"Is 7 even? {calc.is_even(7)}")


if __name__ == "__main__":
    main()
"""
Unit Tests for Calculator Module
Comprehensive test suite for the calculator functionality.
"""

import unittest
import sys
import os

# Add the parent directory to sys.path to import calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(5, -3), 2)
    
    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative numbers."""
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(7, 8), 56)
    
    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(-4, -3), 12)
        self.assertEqual(self.calc.multiply(4, -3), -12)
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333333333, places=10)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)
    
    def test_power_positive_base(self):
        """Test power with positive base."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
    
    def test_power_negative_base(self):
        """Test power with negative base."""
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertEqual(self.calc.power(-2, 3), -8)
    
    def test_power_zero_base(self):
        """Test power with zero base."""
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(0, 0), 1)  # 0^0 = 1 by convention
    
    def test_is_even_positive_numbers(self):
        """Test is_even with positive numbers."""
        self.assertTrue(self.calc.is_even(2))
        self.assertTrue(self.calc.is_even(10))
        self.assertFalse(self.calc.is_even(3))
        self.assertFalse(self.calc.is_even(7))
    
    def test_is_even_negative_numbers(self):
        """Test is_even with negative numbers."""
        self.assertTrue(self.calc.is_even(-2))
        self.assertTrue(self.calc.is_even(-10))
        self.assertFalse(self.calc.is_even(-3))
        self.assertFalse(self.calc.is_even(-7))
    
    def test_is_even_zero(self):
        """Test is_even with zero."""
        self.assertTrue(self.calc.is_even(0))


class TestCalculatorIntegration(unittest.TestCase):
    """Integration tests for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_complex_calculation(self):
        """Test a complex calculation using multiple operations."""
        # ((2 + 3) * 4) / 2 = 10
        result = self.calc.add(2, 3)
        result = self.calc.multiply(result, 4)
        result = self.calc.divide(result, 2)
        self.assertEqual(result, 10)
    
    def test_power_and_even_check(self):
        """Test combining power and even check operations."""
        result = self.calc.power(2, 4)  # 16
        self.assertTrue(self.calc.is_even(result))
        
        result = self.calc.power(3, 3)  # 27
        self.assertFalse(self.calc.is_even(result))


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
"""
Tests for the try_or_try module.
"""

import unittest
from try_or_try import try_or_try


class TestTryOrTry(unittest.TestCase):
    """Test cases for the try_or_try function."""
    
    def test_first_function_succeeds(self):
        """Test that first function's result is returned if it succeeds."""
        def first():
            return "first"
        
        def second():
            return "second"
        
        result = try_or_try(first, second)
        self.assertEqual(result, "first")
    
    def test_second_function_succeeds_after_first_fails(self):
        """Test that second function is tried if first fails."""
        def first():
            raise ValueError("First failed")
        
        def second():
            return "second"
        
        result = try_or_try(first, second)
        self.assertEqual(result, "second")
    
    def test_all_functions_fail(self):
        """Test that last exception is raised if all functions fail."""
        def first():
            raise ValueError("First failed")
        
        def second():
            raise RuntimeError("Second failed")
        
        with self.assertRaises(RuntimeError) as context:
            try_or_try(first, second)
        
        self.assertEqual(str(context.exception), "Second failed")
    
    def test_single_function_succeeds(self):
        """Test with a single function that succeeds."""
        def single():
            return 42
        
        result = try_or_try(single)
        self.assertEqual(result, 42)
    
    def test_single_function_fails(self):
        """Test with a single function that fails."""
        def single():
            raise ValueError("Single failed")
        
        with self.assertRaises(ValueError) as context:
            try_or_try(single)
        
        self.assertEqual(str(context.exception), "Single failed")
    
    def test_no_functions_provided(self):
        """Test that ValueError is raised when no functions are provided."""
        with self.assertRaises(ValueError) as context:
            try_or_try()
        
        self.assertIn("At least one function must be provided", str(context.exception))
    
    def test_multiple_fallbacks(self):
        """Test with multiple fallback functions."""
        def first():
            raise ValueError("First failed")
        
        def second():
            raise RuntimeError("Second failed")
        
        def third():
            return "third"
        
        def fourth():
            return "fourth"
        
        result = try_or_try(first, second, third, fourth)
        self.assertEqual(result, "third")
    
    def test_return_values(self):
        """Test that various return types are handled correctly."""
        def returns_none():
            return None
        
        def returns_false():
            return False
        
        def returns_zero():
            return 0
        
        def returns_empty_string():
            return ""
        
        # All these should succeed even with "falsy" return values
        self.assertIsNone(try_or_try(returns_none))
        self.assertFalse(try_or_try(returns_false))
        self.assertEqual(try_or_try(returns_zero), 0)
        self.assertEqual(try_or_try(returns_empty_string), "")
    
    def test_different_exception_types(self):
        """Test handling of different exception types."""
        def raises_value_error():
            raise ValueError("Value error")
        
        def raises_type_error():
            raise TypeError("Type error")
        
        def raises_key_error():
            raise KeyError("Key error")
        
        def succeeds():
            return "success"
        
        result = try_or_try(
            raises_value_error,
            raises_type_error,
            raises_key_error,
            succeeds
        )
        self.assertEqual(result, "success")


if __name__ == '__main__':
    unittest.main()

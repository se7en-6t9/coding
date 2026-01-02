#!/usr/bin/env python3
"""
Tests for the greeting application
"""

import unittest
from main import greet

class TestGreet(unittest.TestCase):
    """Test cases for the greet function"""
    
    def test_greet_with_hi(self):
        """Test greeting with 'hi'"""
        result = greet("hi")
        self.assertEqual(result, "Hello! How can I help you today?")
    
    def test_greet_with_hi_uppercase(self):
        """Test greeting with 'HI'"""
        result = greet("HI")
        self.assertEqual(result, "Hello! How can I help you today?")
    
    def test_greet_with_hi_mixed_case(self):
        """Test greeting with 'Hi'"""
        result = greet("Hi")
        self.assertEqual(result, "Hello! How can I help you today?")
    
    def test_greet_with_other_message(self):
        """Test greeting with other messages"""
        result = greet("hello")
        self.assertEqual(result, "Hi there!")

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""
Simple greeting application that responds to 'hi'
"""

def greet(message):
    """
    Respond to a greeting message
    
    Args:
        message: Input message string
        
    Returns:
        A friendly response string
    """
    if message.lower().strip() == "hi":
        return "Hello! How can I help you today?"
    return "Hi there!"

def main():
    """Main function to run the greeting application"""
    print("Welcome to the greeting application!")
    print(greet("hi"))

if __name__ == "__main__":
    main()

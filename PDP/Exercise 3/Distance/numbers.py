"""
Numbers Module

This module provides a function to calculate the absolute difference between numbers (integers or floats).

Functions:
- absolute_difference(number1, number2): Calculate the absolute difference between two numbers.

Author: Harishraj S
Date: 27-09-2023
"""

def absolute_difference(number1, number2):
    """
    Calculate the absolute difference between two numbers.

    Args:
        number1 (int or float): The first number.
        number2 (int or float): The second number.

    Returns:
        float: The absolute difference between the two numbers.
    """
    result = abs(number1 - number2)
    return result

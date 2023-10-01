"""
Complex Module

This module provides a function to calculate the absolute difference between complex numbers.

Functions:
- absolute_difference(complex1, complex2): Calculate the absolute difference between two complex numbers.

Author: Harishraj S
Date: 27-09-2023
"""

def absolute_difference(complex1, complex2):
    """
    Calculate the absolute difference between two complex numbers.

    Args:
        complex1 (complex): The first complex number.
        complex2 (complex): The second complex number.

    Returns:
        float: The absolute difference between the two complex numbers.
    """
    result = abs(complex1 - complex2)
    return result

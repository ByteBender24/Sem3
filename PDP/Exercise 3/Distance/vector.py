"""
Vector Module

This module provides functions to calculate distances between n-dimensional points.

Functions:
- euclidean_distance(vector1, vector2): Calculate the Euclidean distance between two n-dimensional vectors.
- manhattan_distance(vector1, vector2): Calculate the Manhattan distance between two n-dimensional vectors.

Author: Harishraj S
Date: 27-09-2023
"""

import math

def euclidean_distance(vector1, vector2):
    """
    Calculate the Euclidean distance between two n-dimensional vectors.

    Args:
        vector1 (list): The first n-dimensional vector.
        vector2 (list): The second n-dimensional vector.

    Returns:
        float: The Euclidean distance between the two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimensions")
    
    squared_diff = sum((x - y) ** 2 for x, y in zip(vector1, vector2))
    distance = math.sqrt(squared_diff)
    return distance

def manhattan_distance(vector1, vector2):
    """
    Calculate the Manhattan distance between two n-dimensional vectors.

    Args:
        vector1 (list): The first n-dimensional vector.
        vector2 (list): The second n-dimensional vector.

    Returns:
        float: The Manhattan distance between the two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimensions")

    distance = sum(abs(x - y) for x, y in zip(vector1, vector2))
    return distance

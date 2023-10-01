"""
Centroid Module

This module provides functions for objects with centroids and calculates distances between centroids.

Classes:
- ObjectWithCentroid: Objects with centroids.

Functions:
- centroid_distance(object1, object2): Calculate the distance between centroids of two objects.

Author: Harishraj S
Date: 27-09-2023
"""

class ObjectWithCentroid:
    def __init__(self, coordinates):
        self.coordinates = coordinates

def centroid_distance(object1, object2):
    """
    Calculate the distance between centroids of two objects.

    Args:
        object1: The first object with a centroid.
        object2: The second object with a centroid.

    Returns:
        float: The distance between the centroids of the two objects.
    """
    centroid1 = sum(object1.coordinates) / len(object1.coordinates)
    centroid2 = sum(object2.coordinates) / len(object2.coordinates)
    distance = abs(centroid1 - centroid2)
    return distance

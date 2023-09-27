'''

The Point class should demonstrate the basic functions using 2D and 3D points.
The class should also have the special functions such as reset, distance, conversion
from 3D to 2D etc.
Create separate packages for 2D and 3D points.

This module consists of Point3D class, where a Point3D object can be created

Author : Harishraj S
Date : 13-09-2023
'''

class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def reset(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def distance(self):
        dist = ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5
        return dist

    def to2D(self):
        from TwoDPoint import Point2D
        return Point2D(self.x, self.y)
    
    def co_ord(self):
        return (self.x, self.y, self.z)
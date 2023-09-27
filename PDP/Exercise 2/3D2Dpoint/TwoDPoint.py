'''

The Point class should demonstrate the basic functions using 2D and 3D points.
The class should also have the special functions such as reset, distance, conversion
from 3D to 2D etc.
Create separate packages for 2D and 3D points.

This module consists of Point2D class, where a Point2D object can be created

Author : Harishraj S
Date : 13-09-2023
'''

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.x = 0
        self.y = 0

    def distance(self):
        dist = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return dist

    def to2D(self, z=0):
        from ThreeDPoint import Point3D
        return Point3D(self.x, self.y, z)
    
    def co_ord(self):
        return (self.x, self.y)
'''
The Point class should demonstrate the basic functions using 2D and 3D points.
The class should also have the special functions such as reset, distance, conversion
from 3D to 2D etc.
Create separate packages for 2D and 3D points.
'''

# Import the classes from their respective modules
from TwoDPoint import Point2D
from ThreeDPoint import Point3D

# Create 2D and 3D points
point_2d = Point2D(3, 4)
point_3d = Point3D(1, 2, 3)

# Test cases for Point2D
print("Point2D:")
print("Coordinates:", point_2d.co_ord())
print("Distance from origin:", point_2d.distance())  
point_3d_converted = point_2d.to2D()
print("Converted to 3D:", point_3d_converted.co_ord()) 
point_2d.reset()
print("After reset - Coordinates:", point_2d.co_ord())  
point_3d_converted = point_2d.to2D()
print("Converted to 3D:", point_3d_converted.co_ord())  

# Test cases for Point3D
print("\nPoint3D:")
print("Coordinates:", point_3d.co_ord())
print("Distance from origin:", point_3d.distance()) 
point_2d_converted = point_3d.to2D()
print("Converted to 2D:", point_2d_converted.co_ord())  
point_3d.reset()
print("After reset - Coordinates:", point_3d.co_ord())  
point_2d_converted = point_3d.to2D()
print("Converted to 2D:", point_2d_converted.co_ord())  

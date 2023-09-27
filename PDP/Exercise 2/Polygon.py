'''
Regular Polygon

3a. Inherit Regular_Polygon from point. Have points_array and num_sides as a
data members and have function for getting details

3b. Inherit any polygon from Regular_Polygon Like square, have additional
functions to calculate area, perimeter and volume

Modification 1 : Added code
Modification 2 : Added documentation and comments
Modification 3 : Updated Driver code
Modification 4 : Formatted document with autopep8

Execution time : [Done] exited with code=0 in 0.218 seconds

Author : Harishraj S
Date : 20-09-2023
'''

from Point import Point
from Circle import Circle
from math import pi

class Polygon(Point):
    """
    A class to represent a polygon.

    Attributes:
        points_array (list of Point): The list of vertices defining the polygon.
        num_sides (int): The number of sides in the polygon.
        center (Point): The center point of the polygon.

    Methods:
        getPolygon(center, points_array, num_sides):
            Update the attributes of the polygon with new values.

    Args:
        points_array (list of Point): List of vertices.
        xcod (float, optional): X-coordinate of the center point. Default is 0.
        ycod (float, optional): Y-coordinate of the center point. Default is 0.
    """
    
    def __init__(self, points_array = [], xcod=0, ycod=0):
        """
        Initialize a Polygon object.

        Args:
            points_array (list of Point): List of vertices defining the polygon.
            xcod (float, optional): X-coordinate of the center point. Default is 0.
            ycod (float, optional): Y-coordinate of the center point. Default is 0.

        Raises:
            ValueError: If the number of points is less than 2.
        """
        if len(points_array) < 2:
            raise ValueError("The given points are not for a polygon, most probably a line or point")       
        super().__init__(xcod, ycod)
        self.points_array = points_array
        self.num_sides = len(points_array)
        self.center = Point(self.xcod, self.ycod)

    def getPolygon(self, center = None, points_array = None, num_sides = None):
        """
        Update the attributes of the polygon with new values.

        Args:
            center (Point, optional): The center point of the polygon.
            points_array (list of Point, optional): List of vertices defining the polygon.
            num_sides (int, optional): The number of sides in the polygon.

        Raises:
            ValueError: If the number of sides is not equal to the length of points_array.
        """
        if center != None:
            self.center = center
        if points_array != None:
            self.points_array = points_array
        if num_sides != None:   
            self.num_sides = num_sides
            
        if self.num_sides != len(self.points_array):
            raise ValueError ("num_sides not in accordance with points_array")

class Square(Polygon):
    """
    A class to represent a square, a specific type of polygon.

    Attributes:
        points_array (list of Point): The list of vertices defining the square.
        center (Point): The center point of the square.

    Methods:
        perimeter():
            Calculate the perimeter of the square.
        area():
            Calculate the area of the square.

    Args:
        points_array (list of Point): List of vertices defining the square.
        xcod (float, optional): X-coordinate of the center point. Default is 0.
        ycod (float, optional): Y-coordinate of the center point. Default is 0.
    """

    def __init__(self, points_array, xcod=0, ycod=0):
        """
        Initialize a Square object.

        Args:
            points_array (list of Point): List of vertices defining the square.
            xcod (float, optional): X-coordinate of the center point. Default is 0.
            ycod (float, optional): Y-coordinate of the center point. Default is 0.

        Raises:
            ValueError: If the number of sides is not equal to 4.
        """
        super().__init__(points_array, xcod, ycod)

    def perimeter(self):
        """
        Calculate the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        # Assuming the square is defined by its four vertices
        if self.num_sides != 4:
            raise ValueError("A square should have 4 sides.")
        side_length = self.center.distance(self.points_array[0])
        return 4 * side_length

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        # Assuming the square is defined by its four vertices
        if self.num_sides != 4:
            raise ValueError("A square should have 4 sides.")
        side_length = self.center.distance(self.points_array[0])
        return side_length ** 2

def square_main():
    """
    Demonstrate the Square class.
    """
    square_points = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
    square = Square(square_points)
    
    print("Square Details:")
    print(f"Perimeter: {square.perimeter()}")
    print(f"Area: {square.area()}")
    print(f"Center: {square.center}")

def polygon_main():
    """
    Demonstrate the Polygon class.
    """
    polygon_points = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
    polygon = Polygon(polygon_points)

    print("Polygon Details:")
    print(f"Number of Sides: {polygon.num_sides}")
    print(f"Center: {polygon.center}")
    print("Vertices:")
    for point in polygon.points_array:
        print(point)

if __name__ == "__main__":
    # Demonstrate the Polygon class
    polygon_main()

    # Demonstrate the Square class
    square_main()

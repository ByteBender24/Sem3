'''
Inherit Circle from point

2a. Create a class called Circle with radius as data member and getCircle(),
calcRad, calcArea() as member functions to read two points, 1.centre, 2.any
point in orbit and calculate the radius and area of the circle.

2b. Create another class called Cone which is derived from the Circle class.
Have a data member apex and utilize the existing data members and the
member functions of the base class by the derived class to find the volume of a
cone ((1/3)*3.14*r*r*h).

Modification 1 : Added code
Modification 2 : Added documentation and comments
Modification 3 : Updated Driver code
Modification 4 : Formatted document with autopep8

Execution time : [Done] exited with code=0 in 0.269 seconds

Author : Harishraj S
Date : 20-09-2023
'''
from math import pi
from Point import Point


class Circle(Point):
    """
    A class representing a two-dimensional circle, inheriting properties from Point.

    Attributes:
        xcod (float): The x-coordinate of the circle's center.
        ycod (float): The y-coordinate of the circle's center.
        radius (float): The radius of the circle.
        point_in_orbit (Point): A point on the orbit of the circle.

    Methods:
        getCircle(center, radius):
            Set new center coordinates and radius for the circle.
        calcRad(pt_rad):
            Calculate and set the radius based on a given point on the orbit.
        calcArea(point_in_orbit):
            Calculate and return the area of the circle.
        __str__():
            Return a string representation of the circle.

    Args:
        xcod (float, optional): Initial x-coordinate of the circle's center. Default is 0.
        ycod (float, optional): Initial y-coordinate of the circle's center. Default is 0.
        radius (float, optional): Initial radius of the circle. Default is 0.
        point_in_orbit (Point, optional): A point on the orbit of the circle. Default is (0,0).
    """

    def __init__(self, xcod=0, ycod=0, radius=0, point_in_orbit: Point = Point(0, 0)):
        """
        Initialize a Circle object.

        Args:
            xcod (float, optional): Initial x-coordinate of the circle's center. Default is 0.
            ycod (float, optional): Initial y-coordinate of the circle's center. Default is 0.
            radius (float, optional): Initial radius of the circle. Default is 0.
            point_in_orbit (Point, optional): A point on the orbit of the circle. Default is (0,0).
        """
        super().__init__(xcod, ycod)
        self.center = Point(self.xcod, self.ycod)
        self.radius = radius
        self.point_in_orbit = point_in_orbit
        if point_in_orbit.showpoint() != (0, 0):
            self.radius = self.center.distance(point_in_orbit)

    def getCircle(self, center: Point = Point(0, 0), radius=0):
        """
        Set new center coordinates and radius for the circle.

        Args:
            center (Point): The new center coordinates of the circle.
            radius (float): The new radius of the circle.
        """
        self.center = center
        self.radius = radius

    def calcRad(self, pt_rad=0):
        """
        Calculate and set the radius based on a given point on the orbit.

        Args:
            pt_rad (float or Point): If a Point is provided, it calculates the radius based on that point.
                If a float is provided, it sets the radius directly.

        Returns:
            float: The calculated or set radius.
        """
        if isinstance(pt_rad, Point):
            self.radius = self.center.distance(pt_rad)
            return self.radius
        self.radius = pt_rad
        return self.radius

    def calcArea(self, point_in_orbit: Point = Point(0, 0)):
        """
        Calculate and return the area of the circle.

        Args:
            point_in_orbit (Point, optional): A point on the orbit of the circle. Default is (0,0).

        Returns:
            float: The area of the circle.
        """
        if point_in_orbit != Point(0, 0):
            self.radius = self.calcRad(point_in_orbit)
        area = pi * (self.radius ** 2)
        return area

    def __str__(self):
        """
        Return a string representation of the circle.

        Returns:
            str: A string containing the center coordinates and radius of the circle.
        """
        return f"Center: {self.center}, Radius: {self.radius}"


class Cone(Circle):
    """
    A class representing a three-dimensional cone, inheriting properties from Circle.

    Attributes:
        xcod (float): The x-coordinate of the cone's base center.
        ycod (float): The y-coordinate of the cone's base center.
        radius (float): The radius of the base circle.
        point_in_orbit (Point): A point on the orbit of the base circle.
        apex (Point): The apex of the cone.
        base_circle (Circle): The base circle of the cone.

    Methods:
        volume(apex):
            Calculate and return the volume of the cone.

    Args:
        xcod (float, optional): Initial x-coordinate of the base center. Default is 0.
        ycod (float, optional): Initial y-coordinate of the base center. Default is 0.
        radius (float, optional): Initial radius of the base circle. Default is 0.
        point_in_orbit (Point, optional): A point on the orbit of the base circle. Default is (0,0).
        apex (Point, optional): The apex of the cone. Default is (0,0).
    """

    def __init__(self, xcod=0, ycod=0, radius=0, point_in_orbit: Point = Point(0, 0), apex=Point(0, 0)):
        """
        Initialize a Cone object.

        Args:
            xcod (float, optional): Initial x-coordinate of the base center. Default is 0.
            ycod (float, optional): Initial y-coordinate of the base center. Default is 0.
            radius (float, optional): Initial radius of the base circle. Default is 0.
            point_in_orbit (Point, optional): A point on the orbit of the base circle. Default is (0,0).
            apex (Point, optional): The apex of the cone. Default is (0,0).
        """
        super().__init__(xcod, ycod, radius, point_in_orbit)
        self.apex = apex
        self.base_circle = Circle(
            self.xcod, self.ycod, self.radius, self.point_in_orbit)

    def volume(self, apex=Point(0, 0)):
        """
        Calculate and return the volume of the cone.

        Args:
            apex (Point, optional): The apex of the cone. Default is (0,0).

        Returns:
            float: The volume of the cone.
        """
        if apex.showpoint() != (0, 0):
            self.apex = apex
        h = self.apex.distance(self.center)
        r = self.radius
        volume = (1 / 3) * pi * r * r * h
        return volume


def circle_main():
    """
    Demonstrate the Circle class by creating two circles, modifying their properties,
    and calculating their radii and areas.
    """
    circle1 = Circle(0, 0, point_in_orbit=Point(0, 2))
    circle2 = Circle(0, 10)
    print(circle1)
    print(circle2)

    center1 = Point(10, 0)
    circle1.getCircle(center=center1)
    print(circle1)
    print(circle2)

    center2 = Point(0, 5)
    point_in_orbit2 = Point(0, 0)
    circle2.getCircle(center=center2)
    print(circle1)
    print(circle2)

    print(f"Rad1: {circle1.calcRad()}, Rad2: {circle2.calcRad(point_in_orbit2)}")
    print(f"Area1: {circle1.calcArea()}, Area2: {circle2.calcArea()}")
    print(circle1)
    print(circle2)


def cone_main():
    """
    Demonstrate the Cone class by creating a cone, setting its properties, and calculating its volume.
    """
    cone = Cone(0, 0, 0, point_in_orbit=Point(2, 0), apex=Point(0, 2))
    print(cone.volume())


if __name__ == "__main__":
    circle_main()
    print()
    print()
    cone_main()

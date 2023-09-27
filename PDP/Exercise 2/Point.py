'''
Create a class Point with xcod and ycod as data members. Include member
functions to read and print the coordinate values as getPoint() and showPoint()
respectively. Write a main method to demonstrate the Point class.

Modification 1 : Added code
Modification 2 : Added documentation and comments
Modification 3 : Updated Driver code
Modification 4 : Formatted document with autopep8

Execution time : [Done] exited with code=0 in 0.179 seconds

Author : Harishraj S
Date : 20-09-2023
'''

class Point:
    """
    A class to represent a point in a two-dimensional Cartesian coordinate system.

    Attributes:
        xcod (float): The x-coordinate of the point.
        ycod (float): The y-coordinate of the point.

    Methods:
        getpoint(xcod, ycod):
            Set new coordinates for the point.
        translate(xdir, ydir):
            Translate the point's coordinates by a given offset.
        showpoint():
            Get the current coordinates of the point.
        distance(other):
            Calculate the Euclidean distance between this point and another point.

    Args:
        xcod (float, optional): Initial x-coordinate of the point. Default is 0.
        ycod (float, optional): Initial y-coordinate of the point. Default is 0.
    """

    def __init__(self, xcod=0, ycod=0):
        """
        Initialize a Point object.

        Args:
            xcod (float, optional): Initial x-coordinate of the point. Default is 0.
            ycod (float, optional): Initial y-coordinate of the point. Default is 0.
        """
        self.xcod = xcod
        self.ycod = ycod

    def getpoint(self, xcod=0, ycod=0):
        """
        Set new coordinates for the point.

        Args:
            xcod (float): The new x-coordinate of the point.
            ycod (float): The new y-coordinate of the point.
        """
        self.xcod = xcod
        self.ycod = ycod

    def translate(self, xdir=0, ydir=0):
        """
        Translate the point's coordinates by a given offset.

        Args:
            xdir (float): The horizontal translation offset.
            ydir (float): The vertical translation offset.
        """
        self.xcod += xdir
        self.ycod += ydir

    def showpoint(self):
        """
        Get the current coordinates of the point.

        Returns:
            tuple: A tuple containing the x and y coordinates of the point.
        """
        return (self.xcod, self.ycod)

    def __str__(self):
        """
        Return a string representation of the point.

        Returns:
            str: A string containing the x and y coordinates of the point.
        """
        return str((self.xcod, self.ycod))

    def distance(self, other):
        """
        Calculate the Euclidean distance between this point and another point.

        Args:
            other (Point): The other point to which the distance is calculated.

        Returns:
            float: The Euclidean distance between this point and the other point.
        """
        dist = ((self.xcod - other.xcod) ** 2 + (self.ycod - other.ycod) ** 2) ** 0.5
        return dist

def point_main():
    """
    Demonstrate the Point class by creating two points, modifying their coordinates,
    and calculating the distance between them.
    """
    p1 = Point()
    p2 = Point()

    print(p1)
    print(p2.showpoint())

    p1.getpoint(4, 3)
    p2.getpoint(2, 2)

    print(p1.showpoint())
    print(p2)

    print(p1.distance(p2))

if __name__ == "__main__":
    point_main()

'''
Write a function called GetRatios(Vec1, Vec2) which reads the values of both the vectors at appropriate indices 
and generates the ratio vector Ratio[]. The Ratio[i] is calculated by Vec1[i] / Vec2[i].
   Write the code for handling exceptions using try, raise, and except in the following conditions:
   (i) When there is a value 'Zero' at some index 'x' of Vec2, place 'NaN' in Ratio[x].
   (ii) When the sizes of both the vectors are different.
   (iii) Create and throw a user-defined exception object when the length of both the vectors is zero.

This program defines a class Ratio_vector that calculates the element-wise ratio of two vectors.
It handles exceptions for zero division, different vector sizes, and zero-size vectors.

Author: Harishraj S
Date: 14-10-2023
'''


from Vector_base import Vector


class DifferentVectorSizeError(Exception):
    def __init__(self, message="Enter vectors of the same size!"):
        super().__init__(message)


class ZeroVectorSizeError(Exception):
    def __init__(self, message="Enter vectors of size other than zero!"):
        super().__init__(message)


class Ratio_vector(Vector):
    def __init__(self, vect1, vect2):
        """
        Initialize a Ratio_vector instance with two input vectors and calculate the element-wise ratio.

        Args:
            vect1 (Vector): The first vector.
            vect2 (Vector): The second vector.

        Raises:
            DifferentVectorSizeError: If the sizes of the input vectors are different.
            ZeroVectorSizeError: If the size of either input vector is zero.
        """
        if len(vect1) != len(vect2):
            raise DifferentVectorSizeError
        if len(vect1) == 0 or len(vect2) == 0:
            raise ZeroVectorSizeError

        self.ratio_vector = []

        try:
            for idx in range(len(vect1)):
                if vect2[idx] == 0:
                    self.ratio_vector.append('NaN')
                else:
                    self.ratio_vector.append(vect1[idx] / vect2[idx])
        except ZeroDivisionError:
            self.ratio_vector = 'NaN'

    def getratios(self, vect1, vect2):
        """
        Calculate the element-wise ratio of two vectors.

        Args:
            vect1 (Vector): The first vector.
            vect2 (Vector): The second vector.

        Raises:
            DifferentVectorSizeError: If the sizes of the input vectors are different.
            ZeroVectorSizeError: If the size of either input vector is zero.
        """
        self.__init__(vect1, vect2)

    def __str__(self) -> str:
        """
        Return the string representation of the calculated ratio vector.

        Returns:
            str: The string representation of the ratio vector.
        """
        return str(self.ratio_vector)


def main():
    # Test cases
    # Test case 1: Equal size vectors, no zero division
    v1 = Vector(1, 2, 3, 4)
    v2 = Vector(2, 1, 4, 1)
    ratio_obj = Ratio_vector(v1, v2)
    print("Element-wise Ratios:", ratio_obj)

    # Usage of "getratios" method
    v1 = Vector(1, 2, 3, 4)
    v2 = Vector(1, 2, 3, 4)
    ratio_obj.getratios(v1, v2)
    print("Element-wise Ratios:", ratio_obj)

    # Test case 2: Vectors with different sizes
    v3 = Vector(1, 2, 3, 4)
    v4 = Vector(1, 2, 3)
    try:
        ratio_obj = Ratio_vector(v3, v4)
    except DifferentVectorSizeError as e:
        print(e)

    # Test case 3: Vectors with size zero
    v5 = Vector()
    v6 = Vector()
    try:
        ratio_obj = Ratio_vector(v5, v6)
    except ZeroVectorSizeError as e:
        print(e)


if __name__ == "__main__":
    main()

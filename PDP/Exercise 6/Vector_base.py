'''
1. Define a vector inheriting from the standard list. Let the vector be restricted to having only integer numbers in the list. Overload appropriate functions and operators so that when any other type of element is inserted, the program raises an error.

2. Write a Python program to overload the operators '+' and '-' to add and subtract two vectors respectively.
   Example:
   - V1 = [2,3,4]
   - V2 = [1]
   - V1 + V2 = [3, 3, 4]
   - V1 - V2 = [1, 3, 4] (Odd Register numbered Students)

3. Write another program to overload the operators '+' and '-' operator to result with the following definitions.
   Example:
   - V1 = [2,3,4]
   - V2 = [1,2]
   - V1 + V2 = [1, 2, 3, 4] (Merge two lists in ascending order without any duplicates)
   - V1 - V2 = [1, 2, 3] (The new vector has items that are different in both the vectors)

4. Write a function called GetRatios(Vec1, Vec2) which reads the values of both the vectors at appropriate indices and generates the ratio vector Ratio[]. The Ratio[i] is calculated by Vec1[i] / Vec2[i].
   Write the code for handling exceptions using try, raise, and except in the following conditions:
   (i) When there is a value 'Zero' at some index 'x' of Vec2, place 'NaN' in Ratio[x].
   (ii) When the sizes of both the vectors are different.
   (iii) Create and throw a user-defined exception object when the length of both the vectors is zero.

Author: Harishraj S
Date: 11-10-2023
'''

from collections.abc import Iterable


class Vector(list):
    def __init__(self, *args: int):
        '''
        Initialize a vector with integer elements.

        Args:
        *args: Variable-length list of integers to initialize the vector.

        Raises:
        TypeError: If any element in *args is not an integer.
        '''
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Enter integer objects only (int)")
        super().__init__(args)

    def append(self, obj: int):
        '''
        Append an integer to the vector.

        Args:
        obj (int): The integer to append to the vector.

        Raises:
        TypeError: If obj is not an integer.
        '''
        if not isinstance(obj, int):
            raise TypeError("Enter integer objects only (int)")
        super().append(obj)

    def extend(self, vect: "list or Vector"):
        '''
        Extend the vector with elements from a list or another Vector.

        Args:
        vect (list or Vector): The list or Vector to extend the vector with.

        Raises:
        TypeError: If any element in vect is not an integer when vect is a list.
        '''
        if isinstance(vect, list) and not isinstance(vect, Vector):
            for obj in vect:
                if not isinstance(obj, int):
                    raise TypeError("Enter a list with integer (int) objects")
            super().extend(vect)
        if isinstance(vect, Vector):
            super().extend(vect)

    def __add__(self, vect: "Vector"):
        '''
        Overload the '+' operator to add two vectors.

        Args:
        vect (Vector): The Vector to add to the current vector.

        Returns:
        Vector: A new Vector containing the elements of the current vector and vect.

        Example:
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5)
        v3 = v1 + v2  # Result: v3 = Vector(1, 2, 3, 4, 5)
        '''

        # Actually no need to do this at all, already defined there in list

        super().extend(vect)
        return self

    def __sub__(self, vect: "Vector"):
        '''
        Overload the '-' operator to subtract two vectors.

        Args:
        vect (Vector): The Vector to subtract from the current vector.

        Returns:
        Vector: A new Vector containing the elements of the current vector that are not in vect.

        Example:
        v1 = Vector(1, 2, 3)
        v2 = Vector(2, 3, 4)
        v3 = v1 - v2  # Result: v3 = Vector(1)
        '''

        # def __sub__ (self, vect:"Vector"):
        #     for obj in self:
        #         if obj in vect:
        #             self.remove(obj)
        #     return self

        # Note : Should not mess with the original list and disturb its index, so create a new list and return it
        new_list = Vector()
        for obj_i in range(len(self)):
            if self[obj_i] not in vect:
                new_list.append(self[obj_i])
        return new_list


def main():
    v = Vector(1, 2, 3, 4, 5, 6, 7, 8, 9)
    v.append(10)
    print(v)

    v.extend([11, 22])
    print(v)

    v1 = Vector(99, 88)
    v.extend(v1)
    print(v)

    v3 = v1 + v1
    print(v3)

    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 3, 4)
    v3 = v1 - v2
    print(v3)


if __name__ == "__main__":
    main()

'''
Write a Python program to overload the operators '+' and '-' to add and subtract two vectors respectively.

This program demonstrates operator overloading for adding and subtracting two vectors using Python's special methods.

Ex. V1 = [2, 3, 4], V2 = [1]
- V1 + V2 = [3, 5, 4]
- V1 - V2 = [1, 1, 4]

Author: Harishraj S
Date: 14-10-2023
'''

from Vector_base import Vector

class Vector_diffSub(Vector):
    def __add__(self, vect: Vector):
        '''
        Overload the '+' operator to add two vectors element-wise.

        Args:
        vect (Vector): The Vector to add to the current vector.

        Returns:
        list: A new list containing the result of the addition.

        Example:
        v1 = Vector_diffSub(1, 2, 3)
        v2 = Vector_diffSub(1, 2)
        result = v1 + v2  # Result: [2, 4, 3]
        '''
        newlist = []
        index_len_max = max([len(self), len(vect)])
        try:
            for idx in range(index_len_max):
                newlist.append(self[idx] + vect[idx])
        except IndexError:
            for idx2 in range(idx, index_len_max):
                newlist.append(self[idx])    
        return newlist
    
    def __sub__(self, vect: Vector):
        '''
        Overload the '-' operator to subtract two vectors element-wise.

        Args:
        vect (Vector): The Vector to subtract from the current vector.

        Returns:
        list: A new list containing the result of the subtraction.

        Example:
        v1 = Vector_diffSub(1, 2, 3)
        v2 = Vector_diffSub(1, 2)
        result = v1 - v2  # Result: [0, 0, 3]
        '''
        newlist = Vector()
        index_len_max = max([len(self), len(vect)])
        try:
            for idx in range(index_len_max):
                newlist.append(self[idx] - vect[idx])
        except IndexError:
            for idx2 in range(idx, index_len_max):
                newlist.append(self[idx])
        return newlist

def main():
    v1 = Vector_diffSub(1, 2, 3)
    v2 = Vector_diffSub(1, 2)

    print(v1 - v2)
    print(v1 + v2)

if __name__ == "__main__":
    main()

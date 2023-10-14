'''
Write another program to overload the operators '+' and '-' operator to result with the following definitions.
   Example:
   - V1 = [2,3,4]
   - V2 = [1,2]
   - V1 + V2 = [1, 2, 3, 4] (Merge two lists in ascending order without any duplicates)
   - V1 - V2 = [3,4] (The new vector has items that are different in both the vectors)

Author: Harishraj S
Date: 14-10-2023
'''

from Vector_base import Vector

class Vector_diffAdd(Vector):
    
   def __add__(self, vect: Vector):
      """
      Overloaded '+' operator to merge two vectors and return a new vector in ascending order without duplicates.

      Args:
         vect (Vector): The vector to be added to the current vector.

      Returns:
         Vector: A new vector containing the merged elements.

      Example:
         v1 = Vector_diffAdd(2, 3, 4)
         v2 = Vector_diffAdd(1, 2)
         result = v1 + v2
         print(result)  # Output: [1, 2, 3, 4]
      """
      # Create a new list to store the result
      newlist = Vector()
      
      # Extend the new list with elements from the first vector
      newlist.extend(self)
      
      # Iterate through elements in the second vector
      for obj in vect:
         # Add the element to the new list if it's not already present
         if obj not in newlist:
            newlist.append(obj)
      
      # Sort the new list in ascending order
      newlist.sort()
      
      return newlist

   def __sub__(self, vect : Vector):
      """
      Overloaded '-' operator to create a new vector containing elements that are different in both vectors.

      Args:
         vect (Vector): The vector to be subtracted from the current vector.

      Returns:
         Vector: A new vector containing elements present in the current vector but not in the other vector.

      Example:
         v1 = Vector_diffAdd(2, 3, 4)
         v2 = Vector_diffAdd(1, 2)
         result = v1 - v2
         print(result)  # Output: [3, 4]
      """
      # Create sets from both vectors to perform set difference
      set1 = set(self)
      set2 = set(vect)
      
      # Calculate the set difference (elements in set1 but not in set2)
      set_diff = set1 - set2
      
      # Convert the result set back to a Vector
      return Vector(*set_diff)

def main():
   # Create instances of Vector_diffAdd
   v1 = Vector_diffAdd(2, 3, 4)
   v2 = Vector_diffAdd(1, 2)
   
   # Demonstrate overloading of '+' and '-' operators
   print("V1 + V2:", v1 + v2)
   print("V1 - V2:", v1 - v2)

if __name__ == "__main__":
   main()
"""
Main Function

This script provides a main function that demonstrates how to use the functions from the Distance package to calculate distances between various objects.

Author: Harishraj S
Date: 27-09-2023
"""

from Distance import vector, complex, centroid, numbers, string


def main():
    # Vector module
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    euclidean_dist = vector.euclidean_distance(vector1, vector2)
    manhattan_dist = vector.manhattan_distance(vector1, vector2)

    print("Vector Module:")
    print(f"Euclidean Distance: {euclidean_dist}")
    print(f"Manhattan Distance: {manhattan_dist}")

    # Complex module
    complex1 = 3 + 4j
    complex2 = 1 + 2j

    abs_diff = complex.absolute_difference(complex1, complex2)

    print("\nComplex Module:")
    print(f"Absolute Difference: {abs_diff}")

    # Centroid module
    object1 = centroid.ObjectWithCentroid([1, 2, 3])
    object2 = centroid.ObjectWithCentroid([4, 5, 6])

    centroid_dist = centroid.centroid_distance(object1, object2)

    print("\nCentroid Module:")
    print(f"Centroid Distance: {centroid_dist}")

    # Numbers module
    number1 = 3
    number2 = 7

    abs_num_diff = numbers.absolute_difference(number1, number2)

    print("\nNumbers Module:")
    print(f"Absolute Number Difference: {abs_num_diff}")

    # String module
    string1 = "kitten"
    string2 = "sitting"

    levenshtein_dist = string.levenshtein_distance(string1, string2)

    print("\nString Module:")
    print(f"Levenshtein Distance: {levenshtein_dist}")


if __name__ == "__main__":
    main()

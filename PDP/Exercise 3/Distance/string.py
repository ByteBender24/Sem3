"""
String Module

This module provides a function to calculate the Levenshtein distance between strings.

Functions:
- levenshtein_distance(string1, string2): Calculate the Levenshtein distance between two strings.

Author: Harishraj S
Date: 27-09-2023
"""

def levenshtein_distance(string1, string2):
    """
    Calculate the Levenshtein distance between two strings.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    if len(string1) < len(string2):
        return levenshtein_distance(string2, string1)

    if len(string2) == 0:
        return len(string1)

    previous_row = range(len(string2) + 1)
    for i, char1 in enumerate(string1):
        current_row = [i + 1]
        for j, char2 in enumerate(string2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (char1 != char2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

"""
 To do the given exercise using the regular expression concept

Author : Harishraj S
Date : 09-11-2023

"""

import re


def is_valid_variable(variable):
    """
    Check the given string can be a valid Variable.
    Sample Test cases:
    Partial_Sum1 - Valid
    1Partial - Invalid
    """
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable) is not None


if __name__ == "__main__":
    variable_name = input("Enter a variable name: ")

    if is_valid_variable(variable_name):
        print("Valid variable name")
    else:
        print("Invalid variable name")

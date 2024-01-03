"""
 To do the given exercise using the regular expression concept

Author : Harishraj S
Date : 09-11-2023

"""

import re


def is_valid_binary_number(binary_number):
    '''
    Validate the given number as a binary number
    Sample Test Cases
    01010 - Valid
    00102 - Invalid
    '''
    return all(char in '01' for char in binary_number)


if __name__ == "__main__":
    binary_number = input("Enter a binary number: ")

    if is_valid_binary_number(binary_number):
        print("Valid binary number")
    else:
        print("Invalid binary number")

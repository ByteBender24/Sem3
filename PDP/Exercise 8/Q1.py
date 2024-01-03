"""
 To do the given exercise using the regular expression concept

Author : Harishraj S
Date : 09-11-2023

"""

import re


def is_valid_password(password):
    '''Check the given string can be a valid password'''

    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True


if __name__ == "__main__":
    password = input("Enter a password: ")

    if is_valid_password(password):
        print("Valid password")
    else:
        print("Invalid password")

'''
Validity Module which provides functions for checking the validity of time and date formats.
• IsValid(Time)
• IsValid(Date)

Author: Harishraj S
Date: 27-09-2023
'''

from datetime import datetime


def is_valid_time(time_str):
    """
    Check if a time string is in a valid format "HH:MM:SS".

    This function checks if a given time string is in the valid format "HH:MM:SS".

    Args:
        time_str (str): The time string to check.

    Returns:
        bool: True if the time string is valid, False otherwise.

    Example:
        >>> is_valid_time("12:34:56")
        True
    """
    try:
        datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False


def is_valid_date(date_str, format="%d.%m.%Y"):
    """
    Check if a date string is in a valid format.

    This function checks if a given date string is in the valid format specified by the 'format' argument.

    Args:
        date_str (str): The date string to check.
        format (str, optional): The expected format of the date string (default is "%d.%m.%Y").

    Returns:
        bool: True if the date string is valid, False otherwise.

    Example:
        >>> is_valid_date("27.09.2023")
        True
    """
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    if is_valid_time("12:34:56"):
        print("Valid time format")
    else:
        print("Invalid time format")

    if is_valid_time("25:00:00"):
        print("Valid time format")
    else:
        print("Invalid time format")

    if is_valid_date("27.09.2023"):
        print("Valid date format")
    else:
        print("Invalid date format")

    if is_valid_date("2023-09-27", "%Y-%m-%d"):
        print("Valid date format")
    else:
        print("Invalid date format")

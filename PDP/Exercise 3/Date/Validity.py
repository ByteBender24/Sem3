'''
Validity Module has the following operations.
• IsValid(Time)
• IsValid(Date)

Author : Harishraj S
Date : 27-09-2023
'''

from datetime import datetime

def is_valid_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False

def is_valid_date(date_str, format="%d.%m.%Y"):
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


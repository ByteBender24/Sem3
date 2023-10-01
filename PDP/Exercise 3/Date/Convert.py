'''
Convert Module has the following operations.
• Convert_hrs_days(#hours)
• Convert_days_hours(#days)
• Convert_man_hrs_days(#hours)

Author : Harishraj S
Date : 27-09-2023
'''


def convert_hrs_days(hours):
    """
    Convert hours to days.

    This function takes the number of hours as input and converts it to days.
    If the input is greater than or equal to 24 hours, it calculates the equivalent
    number of days and returns it rounded to two decimal places. If the input is less
    than 24 hours, it provides a message indicating the fraction of a day given.

    Args:
        hours (float): The number of hours to convert to days.

    Returns:
        float or str: The converted value in days (rounded to two decimal places)
        or a message if the input is less than 24 hours.

    Example:
        >>> convert_hrs_days(30)
        1.25
    """
    if hours >= 24:
        days = hours/24
        return round(days, 2)
    return f"It is less than a day, {round (hours/24,2)} of a day is given"


def convert_days_hours(days):
    """
    Convert days to hours.

    This function takes the number of days as input and converts it to hours.

    Args:
        days (float): The number of days to convert to hours.

    Returns:
        float: The converted value in hours.

    Example:
        >>> convert_days_hours(3)
        72.0
    """
    return days * 24


def convert_man_hrs_days(hours):
    """
    Convert man-hours to days.

    This function takes the number of man-hours as input and converts it to days.
    If the input is greater than or equal to 8 man-hours, it calculates the equivalent
    number of days and returns it rounded to two decimal places. If the input is less
    than 8 man-hours, it provides a message indicating the fraction of a man-hour day given.

    Args:
        hours (float): The number of man-hours to convert to days.

    Returns:
        float or str: The converted value in days (rounded to two decimal places)
        or a message if the input is less than 8 man-hours.

    Example:
        >>> convert_man_hrs_days(16)
        2.0
    """
    if hours >= 8:
        days = hours/8
        return round(days, 2)
    return f"It is less than a man hour day,\n{round (hours/8,2)} of a man hour day is given"


def convert_days_years(days):
    """
    Convert days to years (approximate).

    This function takes the number of days as input and converts it to approximate years.
    It divides the number of days by 365 to estimate the number of years.

    Args:
        days (float): The number of days to convert to years.

    Returns:
        int: The approximate number of years.

    Example:
        >>> convert_days_years(730)
        2
    """
    return days // 365


if __name__ == "__main__":
    # Example usage of the conversion functions
    print(convert_days_hours(3))
    print(convert_hrs_days(30))
    print(convert_hrs_days(8))
    print(convert_hrs_days(48))
    print(convert_man_hrs_days(16))
    print(convert_man_hrs_days(30))
    print(convert_man_hrs_days(4))

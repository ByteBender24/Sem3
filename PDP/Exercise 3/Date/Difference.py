'''
Difference Module which provides functions for date and time differences.
• DifferenceWithCurrent(Date)
• Difference(Date1,Date2)
• DaysAfter(#days)
• DaysBefore(#days)
• MonthAfter(#Months)
• MonthBefore(#Month)

Author: Harishraj S
Date: 27-09-2023
'''

from datetime import datetime, timedelta


def difference_with_current(date):
    """
    Calculate the difference in days between a given date and the current date.

    This function takes a date as input and calculates the difference in days between
    that date and the current date. The date can be provided as a string in the format
    "dd.mm.yyyy" or as a datetime.date object.

    Args:
        date (str or datetime.date): The date to calculate the difference from.

    Returns:
        int: The number of days between the given date and the current date.

    Example:
        >>> difference_with_current('24.12.2004')
        6902
    """
    now = datetime.now().date()
    date_obj = date
    if isinstance(date, str):
        date_obj = datetime.strptime(date, "%d.%m.%Y")
    delta = date_obj - now
    return delta.days


def difference(date1, date2):
    """
    Calculate the difference in days between two dates.

    This function takes two dates as input and calculates the difference in days between them.
    The dates can be provided as strings in the format "dd.mm.yyyy" or as datetime.date objects.

    Args:
        date1 (str or datetime.date): The first date.
        date2 (str or datetime.date): The second date.

    Returns:
        int: The number of days between the two dates.

    Example:
        >>> difference('01.01.2000', '31.12.2000')
        365
    """
    date1_obj, date2_obj = date1, date2
    if isinstance(date1, str):
        date1_obj = datetime.strptime(date1, "%d.%m.%Y")
    if isinstance(date2, str):
        date2_obj = datetime.strptime(date2, "%d.%m.%Y")
    delta = date1_obj - date2_obj
    return delta.days


def days_after(days):
    """
    Calculate a date after a specified number of days from the current date.

    This function calculates a date that is a specified number of days after the current date.

    Args:
        days (int): The number of days to add to the current date.

    Returns:
        str: The date after the specified number of days in the format "dd.mm.yyyy".

    Example:
        >>> days_after(10)
        '07.10.2023'
    """
    now = datetime.now()
    future_date = now + timedelta(days=days)
    return future_date.strftime("%d.%m.%Y")


def days_before(days):
    """
    Calculate a date before a specified number of days from the current date.

    This function calculates a date that is a specified number of days before the current date.

    Args:
        days (int): The number of days to subtract from the current date.

    Returns:
        str: The date before the specified number of days in the format "dd.mm.yyyy".

    Example:
        >>> days_before(5)
        '22.09.2023'
    """
    now = datetime.now()
    past_date = now - timedelta(days=days)
    return past_date.strftime("%d.%m.%Y")


def month_after(months):
    """
    Calculate a date after a specified number of months from the current date.

    This function calculates a date that is a specified number of months after the current date.

    Args:
        months (int): The number of months to add to the current date.

    Returns:
        str: The date after the specified number of months in the format "dd.mm.yyyy".

    Example:
        >>> month_after(2)
        '27.11.2023'
    """
    now = datetime.now()
    future_date = now + timedelta(days=30 * months)
    return future_date.strftime("%d.%m.%Y")


def month_before(months):
    """
    Calculate a date before a specified number of months from the current date.

    This function calculates a date that is a specified number of months before the current date.

    Args:
        months (int): The number of months to subtract from the current date.

    Returns:
        str: The date before the specified number of months in the format "dd.mm.yyyy".

    Example:
        >>> month_before(3)
        '27.06.2023'
    """
    now = datetime.now()
    past_date = now - timedelta(days=30 * months)
    return past_date.strftime("%d.%m.%Y")


if __name__ == "__main__":
    # Example usage of the difference and date calculation functions
    print(difference_with_current('24.12.2004'))

    # Test the difference_with_current function
    current_date = datetime.now().strftime("%d.%m.%Y")
    test_date = "24.12.2004"
    days_difference = difference_with_current(test_date)
    print(
        f"Days between {test_date} and current date {current_date}: {days_difference} days")

    # Test the difference function
    date1 = "01.01.2000"
    date2 = "31.12.2000"
    days_difference = difference(date1, date2)
    print(f"Days between {date1} and {date2}: {days_difference} days")

    # Test the days_after function
    days = 10
    future_date = days_after(days)
    print(f"{days} days after current date: {future_date}")

    # Test the days_before function
    days = 5
    past_date = days_before(days)
    print(f"{days} days before current date: {past_date}")

    # Test the month_after function
    months = 2
    future_date = month_after(months)
    print(f"{months} months after current date: {future_date}")

    # Test the month_before function
    months = 3
    past_date = month_before(months)
    print(f"{months} months before current date: {past_date}")

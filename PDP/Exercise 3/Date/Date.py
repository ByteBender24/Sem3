'''
Date Module which provides a Date class for working with dates and date conversion.
• Create and display dates

Author: Harishraj S
Date: 27-09-2023
'''

import datetime


class Date:

    def __init__(self, year, month, date):
        """
        Initialize a Date object with year, month, and date.

        Args:
            year (int): The year component of the date.
            month (int): The month component of the date.
            date (int): The day component of the date.
        """
        self.year = year
        self.month = month
        self.date = date

    def __str__(self):
        """
        Return the date as a string in the "YYYY/MM/DD" format.

        Returns:
            str: The date in "YYYY/MM/DD" format.
        """
        return f"{self.year}/{self.month}/{self.date}"

    def showdate(self):
        """
        Return the date as a string in the "YYYY/MM/DD" format.

        Returns:
            str: The date in "YYYY/MM/DD" format.
        """
        return f"{self.year}/{self.month}/{self.date}"

    def gatedate(self, year, month, date):
        """
        Set the date components to new values.

        Args:
            year (int): The new year component.
            month (int): The new month component.
            date (int): The new day component.
        """
        self.year = year
        self.month = month
        self.date = date


def date_obj_converter(string, format):
    '''
    Convert a date string to a datetime.date object.

    Args:
        string (str): The date string to convert.
        format (str): The format of the date string.

    Returns:
        datetime.date: The date as a datetime.date object.

    Example:
        >>> date_obj_converter('2004/3/24', '%Y/%m/%d')
        datetime.date(2004, 3, 24)
    '''
    date_obj = datetime.datetime.strptime(string, format).date()
    return date_obj


if __name__ == "__main__":
    now_datetime = datetime.datetime.now()
    now_date = datetime.date.today()

    print(now_date)
    print(now_datetime)

    date1 = Date(2004, 3, 24)
    print(date1)

    date_obj = date_obj_converter(date1.showdate(), '%Y/%m/%d')
    print(date_obj)

    help(date_obj_converter)

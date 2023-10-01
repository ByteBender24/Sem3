'''
Current module which provides functions for accessing current date and time in various formats.
• Current time
• Current date default return format dd.mm.yyyy
• Current date in different formats mm.dd.yyyy
• Current date in string format

Author: Harishraj S
Date: 27-09-2023
'''

from datetime import datetime
date_time = datetime.now()


def current_time():
    """
    Get the current time.

    This function retrieves the current time and returns it in the "HH:MM:SS" format.

    Returns:
        str: The current time in "HH:MM:SS" format.

    Example:
        >>> current_time()
        '14:30:45'
    """
    time = date_time.time()
    time = time.strftime("%H:%M:%S")
    return time


def current_date(format="default"):
    """
    Get the current date in different formats.

    This function retrieves the current date and provides it in various formats based on
    the format parameter.

    Args:
        format (str): The format in which the date should be returned. Possible values are:
            - "default": Returns the date in the "dd.mm.yyyy" format.
            - "mm.dd.yyyy": Returns the date in the "mm.dd.yyyy" format.
            - "string": Returns the date as a string in "Day, Month Day, Year" format.

    Returns:
        str: The current date in the specified format.

    Example:
        >>> current_date()
        '27.09.2023'

        >>> current_date("mm.dd.yyyy")
        '09.27.2023'

        >>> current_date("string")
        'Tuesday, September 27, 2023'
    """
    if format == "default":
        return date_time.strftime("%d.%m.%Y")
    elif format == "mm.dd.yyyy":
        return date_time.strftime("%m.%d.%Y")
    elif format == "string":
        return date_time.strftime("%A, %B %d, %Y")


if __name__ == "__main__":
    # Example usage of the current date and time functions
    print(date_time)
    print(current_time())
    print(current_date())
    print(current_date("mm.dd.yyyy"))
    print(current_date("string"))

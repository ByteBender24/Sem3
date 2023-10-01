'''
Current module which may be helpful in getting
• Current time
• Current date default return format dd.mm.yyyy
• Current date in different formats mm.dd.yyyy
• Current date in string format

Author : Harishraj S
Date : 27-09-2023
'''

from datetime import datetime
date_time = datetime.now()


def current_time():
    time = date_time.time()
    time = time.strftime("%H:%M:%S")
    return time


def current_date(format="default"):

    if format == "default":
        return date_time.strftime("%d.%m.%Y")
    elif format == "mm.dd.yyyy":
        return date_time.strftime("%m.%d.%Y")
    elif format == "string":
        return date_time.strftime("%A, %B %d, %Y")


if __name__ == "__main__":

    print(date_time)
    print(current_time())
    print(current_date())
    print(current_date("mm.dd.yyyy"))
    print(current_date("string"))
